from manim import *
import math

# Creamos figuras y se seccionan con plano


def create_rectangles(
    num_rectangles,
    color=BLUE,
    width=1,
    height=10,
    opacity=0.4,
    stroke_color=None,
    stroke_width=1,
    stroke_opacity=1,
):
    rectangles = VGroup()
    for i in range(num_rectangles):
        rect = (
            Rectangle(color=color, width=width, height=height)
            .set_opacity(opacity)
            .set_stroke(BLUE, stroke_width, stroke_opacity)
        )
        if i == 0:
            rect.move_to([-4.5, 0, 0])

        if i > 0:
            rect.next_to(rectangles[i - 1], RIGHT, buff=0)
        rectangles.add(rect)
    return rectangles


class Scene1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES, zoom=1)
        line_length = 0.1
        rectangulos = create_rectangles(100,width=line_length)
        Ejes = ThreeDAxes()
        labels = Ejes.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45), Text("z").scale(0.45)
        )

        num_lines = 150000

        

        lines = VGroup()
        cortes = 0

        for _ in range(num_lines):
            angle = np.random.uniform(0, 360) * DEGREES
       
            x = np.random.uniform(-4, 4)
            y = np.random.uniform(-4, 4)
            x2 = line_length * math.cos(angle) + x
            y2 = line_length * math.sin(angle) + y
            
            for object in rectangulos:
                cordenada = object.get_vertices()

                if (
                    x <= cordenada[0][0]
                    and cordenada[0][0] <= x2
                    or x2 <= cordenada[0][0]
                    and cordenada[0][0] <= x
                ):
                    if (
                        y <= cordenada[0][1]
                        and cordenada[2][1] <= y
                        or y2 <= cordenada[0][1]
                        and cordenada[2][1] <= y2
                    ):
                        cortes += 1

            z = 0

            # line = Line(
            #     [x, y, z],
            #     [x2, y2, z],
            # )

            # lines.add(line)
        num_cortes = Text("Cortes=" + str(cortes)).to_edge(RIGHT + UP).scale(0.7)
        lanzamientos = (
            Text("Lanzamientos=" + str(num_lines)).next_to(num_cortes, DOWN).scale(0.5)
        )
        aprox = (
            Text("pi=" + str(round((2 * num_lines) / cortes, 7)))
            .next_to(lanzamientos, DOWN)
            .scale(0.6)
        )
        self.add_fixed_in_frame_mobjects(num_cortes, lanzamientos, aprox)
        Ejes = ThreeDAxes()

        self.add(rectangulos, Ejes, lines)

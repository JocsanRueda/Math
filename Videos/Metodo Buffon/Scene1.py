from manim import *
import math


# Funcion  que crea rectangulos uno al lado del otro
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
        # se ajusta la posicion de la camara
        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES, zoom=1)

        # largo de la linea
        line_length = 1

        # relacion de proporcion del ancho de los rectangulos
        rect_length = 1

        # Numero de lineas
        num_lines = 10
        rectangulos = create_rectangles(
            int(10 / (line_length * rect_length)), width=line_length * rect_length
        )

        # Ejes
        Ejes = ThreeDAxes()
        labels = Ejes.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45), Text("z").scale(0.45)
        )

        # Array que contiene las lineas
        lines = VGroup()
        # Cortes
        cortes = 0

        # linea que servira de guia
        angle = 30 * DEGREES

        x = -0.1
        y = -0.5
        x2 = line_length * math.cos(angle) + x
        y2 = line_length * math.sin(angle) + y
        linea_guia = Line([x, y, 0],[x2,y2,0])
        self.add(linea_guia)
        for _ in range(num_lines):
            angle = np.random.uniform(0, 360) * DEGREES

            x = np.random.uniform(-4, 4)
            y = np.random.uniform(-4, 4)
            x2 = line_length * math.cos(angle) + x
            y2 = line_length * math.sin(angle) + y

            for object in rectangulos:
                cordenada = object.get_vertices()
                # Comprobacion si una linea c un rectangulo
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
            # posicion del ejej z
            z = 0

            # line = Line(
            #     [x, y, z],
            #     [x2, y2, z],
            # )

            # lines.add(line)

        # texto que muestra el numero de cortes
        num_cortes = Text("Cortes=" + str(cortes)).to_edge(RIGHT + UP).scale(0.7)

        # Texto que muestra el numero de lanzamientos
        lanzamientos = (
            Text("Lanzamientos=" + str(num_lines)).next_to(num_cortes, DOWN).scale(0.5)
        )

        # aproximacion generada de pi
        aprox = (
            MathTex(
                r"\pi \approx"
                + str(
                    round(
                        (2 * num_lines * line_length)
                        / (cortes * line_length * rect_length),
                        7,
                    )
                )
            )
            .next_to(lanzamientos, DOWN)
            .scale(0.8)
        )

        # se fijan los textos para que siempre vean a camara
        self.add_fixed_in_frame_mobjects(num_cortes, lanzamientos, aprox)
        self.add(rectangulos, lines)
        self.wait()
        self.move_camera(phi=0, theta=-PI/2)
        self.wait()
        self.move_camera(phi=0,theta=-PI/2,frame_center=linea_guia,zoom=3.8 )
        self.wait() 

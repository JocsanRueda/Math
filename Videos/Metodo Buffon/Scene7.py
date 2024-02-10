
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


def generate_lineas(num_lines, line_length, rectangulos):
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

        line = Line(
            [x, y, z],
            [x2, y2, z],
        )

        lines.add(line)
    return lines, cortes


class Scene7(ThreeDScene):
    def construct(self):
        # se ajusta la posicion de la camara





        # largo de la linea
        line_length = 1

        # relacion de proporcion del ancho de los rectangulos
        rect_length = 1.1

        # Numero de lineas
        num_lines = 10
        rectangulos = create_rectangles(int(10 / (rect_length)), width=rect_length)

        # Ejes
        Ejes = ThreeDAxes()
        labels = Ejes.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45), Text("z").scale(0.45)
        )

        # linea que servira de guia
        angle = 30 * DEGREES

        x = rectangulos[4].get_vertices()[0][0] - 0.1
        y = -0.5
        x2 = line_length * math.cos(angle) + x
        y2 = line_length * math.sin(angle) + y
        z = 0
        linea_guia = Line([x, y, z], [x2, y2, z], color=WHITE)



        self.add(rectangulos,linea_guia)

        self.set_camera_orientation(phi=0 * DEGREES, theta=-PI/2, zoom=3.8,frame_center=linea_guia)
        self.wait()
        self.move_camera(phi=60*DEGREES, theta=-70*DEGREES, frame_center=ORIGIN, zoom=1)
        self.begin_ambient_camera_rotation(rate=0.05, about="theta")
        self.wait(3)
        l = [50000,100000,200000]
        # texto que muestra el numero de cortes
        oldObject = VGroup()

        for i in range(len(l)):
            lineas, cortes = generate_lineas(l[i], line_length, rectangulos)

            # Texto que muestra el numero de lanzamientos
            lanzamientos = (
                MathTex(r"\text{Lanzamientos}=" + f"{l[i]:,}")
                .to_edge(RIGHT + UP)
                .shift([1, 0, 0])
                .scale(0.7)
            )

            # texto que muestra el numero de cortes
            num_cortes = (
                MathTex(r"\text{Cortes}=" + f"{cortes :,}")
                .next_to(lanzamientos, DOWN)
                .scale(0.7)
            )

            # aproximacion generada de pi
            pi_aprox = round(
                (2 * l[i] * line_length) / (cortes * rect_length),
                5,
            )
            aprox = (
                MathTex(r"\pi \approx" + str(pi_aprox))
                .next_to(num_cortes, DOWN)
                .scale(0.7)
            )

            if i == 0:
                oldObject.add(num_cortes, lanzamientos, aprox, lineas)

                # se fijan los textos para que siempre vean a camara
                self.add_fixed_in_frame_mobjects(num_cortes, lanzamientos, aprox)
                num_cortes.set_opacity(0)
                aprox.set_opacity(0)
                lanzamientos.set_opacity(0)
                self.play(
                    FadeOut(linea_guia),
                    Create(lineas),
                    FadeIn(num_cortes),
                    FadeIn(lanzamientos),
                    FadeIn(aprox),
                    num_cortes.animate.set_opacity(1),
                    lanzamientos.animate.set_opacity(1),
                    aprox.animate.set_opacity(1),
                )
                self.wait()

            else:
                self.add_fixed_in_frame_mobjects(num_cortes, aprox, lanzamientos)
                num_cortes.set_opacity(0)
                aprox.set_opacity(0)
                lanzamientos.set_opacity(0)
                self.play(
                    (Create(linea_guia) if i == len(l)-1 else Create(Tex())),
                    ReplacementTransform(oldObject[-1], lineas),
                    ReplacementTransform(oldObject[0], num_cortes),
                    ReplacementTransform(oldObject[1], lanzamientos),
                    ReplacementTransform(oldObject[2], aprox),
                    num_cortes.animate.set_opacity(1),
                    lanzamientos.animate.set_opacity(1),
                    aprox.animate.set_opacity(1),
                )

                oldObject.remove(*oldObject)
                oldObject.add(num_cortes, lanzamientos, aprox, lineas)
                self.wait()

        self.wait(4)
        self.play(*[Uncreate(obj) for obj in oldObject])

        self.wait()


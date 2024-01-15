from manim import *
import math


def puntos_equidistantes(punto1, punto2, n):
    """
    Encuentra n puntos equidistantes entre dos puntos tridimensionales.

    Parameters:
    punto1 (np.array): Primer punto tridimensional (x1, y1, 0).
    punto2 (np.array): Segundo punto tridimensional (x2, y2, 0).
    n (int): Número de puntos equidistantes deseados.

    Returns:
    np.array: Matriz con n puntos equidistantes.
    """
    distancia_total = np.linalg.norm(punto2[:2] - punto1[:2])
    paso = distancia_total / (n + 1)

    direccion = (punto2[:2] - punto1[:2]) / distancia_total

    puntos = []
    for i in range(1, n + 1):
        punto_intermedio = punto1[:2] + i * paso * direccion
        punto_equidistante = np.array([punto_intermedio[0], punto_intermedio[1], 0])
        puntos.append(punto_equidistante)

    return np.array(puntos)


def create_rectangles(
    num_rectangles,
    color=BLUE,
    width=1,
    height=10,
    opacity=0.1,
    stroke_color=None,
    stroke_width=0.30,
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


class Scene2(MovingCameraScene):
    def construct(self):
        line_length = 1

        # relacion de proporcion del ancho de los rectangulos
        rect_length = 1

        # Numero de lineas
        num_lines = 10
        rectangulos = create_rectangles(
            int(10 / (line_length * rect_length)), width=line_length * rect_length
        )
        angle = 30 * DEGREES
        # -0.1 valor original
        x = -0.1
        y = -0.5
        x2 = line_length * math.cos(angle) + x
        y2 = line_length * math.sin(angle) + y
        linea_guia = Line([x, y, 0], [x2, y2, 0], stroke_width=1)
        b1 = Brace(
            linea_guia,
            direction=linea_guia.copy().rotate(270 * DEGREES).get_unit_vector(),
            sharpness=4,
            stroke_width=0,
            buff=0.1,
        ).scale(0.9)
        b1Text = b1.get_tex("k").scale(0.4).shift([-0.25, 0.3, 0])

        puntos = linea_guia.get_all_points()
        centro = Dot(puntos_equidistantes(puntos[0], puntos[-1], 1)).scale(0.2)
        # punto interseccion
        pi = Dot([rectangulos[4].get_vertices()[0][0], -0.25, 0]).scale(0.2)
        # linea de intercescion puinteada x
        linea_interseccion = DashedLine(
            pi, centro, dash_length=0.02, stroke_width=1, color=YELLOW_C
        )

        # texto variable x
        f1 = MathTex(r"x").next_to(linea_interseccion, UP, buff=0.02).scale(0.35)
        # acotacion de variable x
        f2 = (
            MathTex(r"0\leqslant x \leqslant \frac{d}{2}")
            .scale(0.28)
            .next_to(f1, RIGHT, buff=0.7)
            .shift([0.2, 0.5, 0])
        )

        # distancia entre las lineas
        dp1 = Dot([rectangulos[4].get_vertices()[0, 0], 0.3, 0]).scale(0.2)
        dp2 = Dot([rectangulos[5].get_vertices()[0, 0], 0.3, 0]).scale(0.2)

        # distancia d

        distancia_lineas = DashedLine(
            dp1, dp2, stroke_width=1, dash_length=0.02, color=YELLOW_C
        ).add(dp1, dp2)
        f3 = MathTex(r"d").next_to(distancia_lineas, UP, buff=0.001).scale(0.35)
        # relacion distancia d
        f4 = (
            MathTex(r"k\leqslant d")
            .scale(0.28)
            .next_to(f3, RIGHT, buff=0.1)
            .shift([0.6, 0, 0])
        )
        # angulo

        angulo = Angle(
            linea_guia,
            Line(Dot(ORIGIN), Dot([0, -1, 0])),
            quadrant=(1, -1),
            radius=0.2,
            stroke_width=1,
            color=BLUE,
        )
        # simbolo alfa
        f5 = MathTex(r"\alpha").next_to(angulo, UP, buff=0.01).scale(0.35)
        # acotacion de alfa
        f6 = (
            MathTex(r"0\leqslant Min(\alpha,\theta) \leqslant \frac{\pi}{2}")
            .scale(0.2)
            .next_to(f1, RIGHT, buff=0.7)
            .shift([0.1, 0.5, 0])
        )
        # angulo theta
        angulo2 = Angle(
            Line(Dot(ORIGIN), Dot([0, -1, 0])),
            linea_guia,
            radius=0.2,
            quadrant=(1, 1),
            stroke_width=1,
            color=YELLOW_C,
        )

        # simbolo teta
        f7 = MathTex(r"\theta").scale(0.28).next_to(angulo2, DOWN, buff=0.1)
        self.add(rectangulos, linea_guia)

        self.camera.frame.save_state()
        self.camera.frame.set(width=3.5).move_to(linea_guia)

        # funcion para mover punto linea guia

        def mov_point(obj):
            puntos = linea_guia.get_all_points()
            p1 = puntos[0]
            p2 = puntos[-1]

            centro.move_to(puntos_equidistantes(p1, p2, 1))
            obj.become(
                DashedLine(pi, centro, stroke_width=1, dash_length=0.02, color=YELLOW_C)
            )
            f1.next_to(linea_interseccion, UP, buff=0.095)

        anguloTracker = ValueTracker(30)
        end = False
        print(linea_guia.get_all_points()[0])

        def mov_point_angle(obj):
            puntos = obj.get_all_points()[0]
            x2 = line_length * math.cos(anguloTracker.get_value() * DEGREES) + puntos[0]
            y2 = line_length * math.sin(anguloTracker.get_value() * DEGREES) + puntos[1]

            obj.put_start_and_end_on([puntos[0], puntos[1], 0], [x2, y2, 0])

            angulo.become(
                Angle(
                    linea_guia,
                    Line(Dot(ORIGIN), Dot([0, -1, 0])),
                    quadrant=(1, -1),
                    radius=0.2,
                    stroke_width=1,
                    color=BLUE,
                )
            )
            angulo2.become(
                Angle(
                    Line(Dot(ORIGIN), Dot([0, -1, 0])),
                    linea_guia,
                    radius=0.2,
                    quadrant=(1, 1),
                    stroke_width=1,
                    color=YELLOW_C,
                )
            )
            if not end:
                f5.become(
                    MathTex(
                        r"\alpha = "
                        + str(int(90 - anguloTracker.get_value()))
                        + r"^{\circ}"
                    )
                    .next_to(angulo, UP, buff=0.001)
                    .scale(0.2)
                )
                f7.become(
                    MathTex(
                        r"\theta = "
                        + str(math.ceil(90 + anguloTracker.get_value()))
                        + r"^{\circ}"
                    )
                    .next_to(angulo2, DOWN, buff=0.001)
                    .scale(0.2)
                )

        # se dibuja el largo de las lineas
        self.play(Create(distancia_lineas))
        # se muestra d
        self.play(Write(f3))

        # se muestra k y su brace
        self.play(FadeIn(b1), Write(b1Text))
        # se escribe la restricion k<=d
        self.play(Write(f4))
        self.wait()

        # se borran los elementos creados anteriorment
        self.play(
            Uncreate(distancia_lineas),
            Uncreate(f3),
            FadeOut(b1),
            Uncreate(b1Text),
            Uncreate(f4),
        )
        self.wait()
        # se muestra la distancia x
        self.play(Create(linea_interseccion), Write(f1), Create(pi), Create(centro))
        linea_interseccion.add_updater(mov_point)
        self.play(linea_guia.animate.shift([0.1, 0, 0]))
        self.play(linea_guia.animate.shift([-0.8, 0, 0]))
        self.play(linea_guia.animate.shift([0.7, 0, 0]), Write(f2))
        linea_interseccion.remove_updater(mov_point)

        self.play(Uncreate(pi),Uncreate(centro),Uncreate(linea_interseccion),Uncreate(f1),Uncreate(f2))
        
        self.play(Create(angulo), Write(f5), Create(angulo2), Write(f7))

        linea_guia.add_updater(mov_point_angle)
        self.play(linea_guia.animate.shift([0.1,0,0]))
        self.play(anguloTracker.animate.set_value(anguloTracker.get_value() - 30))
        self.play(anguloTracker.animate.set_value(anguloTracker.get_value() + 89.99999))
        self.play(anguloTracker.animate.set_value(anguloTracker.get_value() - 59.99999))
        self.play(Write(f6))
        end = True
        linea_interseccion.add_updater(mov_point)
        self.play(
            FadeOut(angulo2),
            Uncreate(f7),
            f5.animate.become(MathTex(r"\alpha").scale(0.35))
            .next_to(f1, LEFT)
            .shift([0, -0.25, 0]),
            linea_guia.animate.shift([-0.05,0,0])
        ),
        
        self.play(Create(linea_interseccion), Create(pi), Create(centro), Write(f1))
        f2.next_to(f6, DOWN,buff=0.09)
        self.play(
            f6.animate.become(
                MathTex(r"0\leqslant \alpha \leqslant \frac{\pi}{2}")
                .scale(0.28)
                .next_to(f1, RIGHT, buff=0.7)
                .shift([0.2, 0.5, 0])
            ),
            Write(f2),
        )
        f2.add(f6)
        rect = SurroundingRectangle(f2, TEAL, stroke_width=1)
        self.play(Create(rect))

        self.wait()

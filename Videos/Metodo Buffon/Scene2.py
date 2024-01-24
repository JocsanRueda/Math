from manim import *
import math


def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] + p2[1]) ** 2)


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
    opacity=0.4,
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


line_length = 1

# relacion de proporcion del ancho de los rectangulos
rect_length = 1.1

# Numero de lineas
num_lines = 10
rectangulos = create_rectangles(
    int(10 / (line_length * rect_length)), width=line_length * rect_length
)
angle = 30 * DEGREES
# -0.1 valor original
x = rectangulos[4].get_vertices()[0][0] - 0.1
y = -0.5
x2 = line_length * math.cos(angle) + x
y2 = line_length * math.sin(angle) + y
linea_guia = Line([x, y, 0], [x2, y2, 0], stroke_width=1)
n = 0.3


b1 = Brace(
    linea_guia.copy().scale(n ** (-1)),
    direction=linea_guia.copy().rotate(270 * DEGREES).get_unit_vector(),
    sharpness=2.5,
    stroke_width=-0.5,
    buff=0.1,
).scale(n * 1)
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
    .shift([0.43, 0.5, 0])
)

# distancia entre las lineas
dp1 = Dot([rectangulos[4].get_vertices()[0, 0], 0.3, 0]).scale(0.2)
dp2 = Dot([rectangulos[5].get_vertices()[0, 0], 0.3, 0]).scale(0.2)

dp3 = Dot([rectangulos[3].get_vertices()[0, 0], 0.3, 0]).scale(0.2)
dp4 = Dot([rectangulos[4].get_vertices()[0, 0], 0.3, 0]).scale(0.2)

# distancia d

distancia_lineas = DashedLine(
    dp1, dp2, stroke_width=1, dash_length=0.02, color=YELLOW_C
).add(dp1, dp2)
f3 = MathTex(r"d").next_to(distancia_lineas, UP, buff=0.001).scale(0.35)

distancia_lineas2 = DashedLine(
    dp3, dp4, stroke_width=1, dash_length=0.02, color=YELLOW_C
).add(dp3, dp4)

f3copy = MathTex(r"d").next_to(distancia_lineas2, UP, buff=0.001).scale(0.35)
# relacion distancia d
f4 = (
    MathTex(r"k\leqslant d")
    .scale(0.28)
    .next_to(f3, RIGHT, buff=0.1)
    .shift([0.75, 0, 0])
)
# angulo

angulo = Angle(
    linea_guia,
    Line(Dot([x + 0.1, 0, 0]), Dot([x + 0.1, -1, 0])),
    quadrant=(1, -1),
    radius=0.17,
    stroke_width=1,
    color=BLUE,
)
# simbolo alfa
f5 = MathTex(r"\alpha").next_to(angulo, UP, buff=0.01).scale(0.35)
# acotacion de  alfa
f6 = (
    MathTex(r"0\leqslant Min(\alpha,\theta) \leqslant \frac{\pi}{2}")
    .scale(0.2)
    .next_to(f1, RIGHT, buff=0.7)
    .shift([0.3, 0.5, 0])
)
# angulo theta
angulo2 = Angle(
    Line(Dot([x + 0.1, 0, 0]), Dot([x + 0.1, -1, 0])),
    linea_guia,
    radius=0.17,
    quadrant=(1, 1),
    stroke_width=1,
    color=YELLOW_C,
)

# simbolo teta
f7 = MathTex(r"\theta").scale(0.28).next_to(angulo2, DOWN, buff=0.1)


def mov_point(obj):
    puntos = linea_guia.get_all_points()
    p1 = puntos[0]
    p2 = puntos[-1]

    centro.move_to(puntos_equidistantes(p1, p2, 1))
    d1 = distancia(centro.get_center(), rectangulos[3].get_vertices()[0])
    d2 = distancia(centro.get_center(), rectangulos[4].get_vertices()[0])
    d3 = distancia(centro.get_center(), rectangulos[5].get_vertices()[0])
    menor = min([d1, d2, d3])

    if menor == d1:
        pi.become(
            Dot([rectangulos[3].get_vertices()[0][0], centro.get_y(), 0]).scale(0.2)
        )
    elif menor == d2:
        pi.become(
            Dot([rectangulos[4].get_vertices()[0][0], centro.get_y(), 0]).scale(0.2)
        )
    else:
        pi.become(
            Dot([rectangulos[5].get_vertices()[0][0], centro.get_y(), 0]).scale(0.2)
        )

    obj.become(DashedLine(pi, centro, stroke_width=1, dash_length=0.02, color=YELLOW_C))
    # 0.095
    global buff

    f1.next_to(linea_interseccion, UP, buff=buff)


radio = 0.17
anguloTracker = ValueTracker(30)
end = False

buff = 0.095


def mov_point_angle(obj):
    puntos = obj.get_all_points()[0]
    x2 = line_length * math.cos(anguloTracker.get_value() * DEGREES) + puntos[0]
    y2 = line_length * math.sin(anguloTracker.get_value() * DEGREES) + puntos[1]

    obj.put_start_and_end_on([puntos[0], puntos[1], 0], [x2, y2, 0])

    angulo.become(
        Angle(
            linea_guia,
            Line(Dot([x + 0.1, 0, 0]), Dot([x + 0.1, -1, 0])),
            quadrant=(1, -1),
            radius=radio,
            stroke_width=1,
            color=BLUE,
        )
    )
    angulo2.become(
        Angle(
            Line(Dot([x + 0.1, 0, 0]), Dot([x + 0.1, -1, 0])),
            linea_guia,
            radius=radio,
            quadrant=(1, 1),
            stroke_width=1,
            color=YELLOW_C,
        )
    )
    if not end:
        f5.become(
            MathTex(
                r"\alpha = " + str(int(90 - anguloTracker.get_value())) + r"^{\circ}"
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


class Scene2_0(MovingCameraScene):
    def construct(self):
        self.add(rectangulos, linea_guia)

        self.camera.frame.save_state()
        self.camera.frame.set(width=3.8).move_to(linea_guia)
        self.wait()
        self.play(rectangulos.animate.set_fill(opacity=0))
        # funcion para mover punto linea guia

        # se dibuja el largo de las lineas

        self.play(Create(distancia_lineas))

        # se muestra d
        self.play(Write(f3))

        # # se muestra k y su brace
        self.play(FadeIn(b1), Write(b1Text))
        # se escribe la restricion k<=d
        self.play(Write(f4))
        self.wait()

        # se borran los elementos creados anteriorment
        self.play(
            FadeOut(b1),
            Uncreate(b1Text),
            Uncreate(f4),
        )
        self.wait()
        # se muestra la distancia x

        self.play(Create(linea_interseccion), Write(f1), Create(pi), Create(centro))

        linea_interseccion.add_updater(mov_point)

        self.play(Create(distancia_lineas2), Write(f3copy))
        self.play(linea_guia.animate.shift([0.6, 0, 0]), run_time=1.5)
        self.play(linea_guia.animate.shift([-1.4, 0, 0]), run_time=1.5)
        self.play(linea_guia.animate.shift([0.8, 0, 0]), Write(f2))

        self.play(
            Uncreate(f2),
            Uncreate(distancia_lineas2),
            Uncreate(distancia_lineas),
            Uncreate(f3),
            Uncreate(f3copy),
            Uncreate(centro),
            Uncreate(linea_interseccion),
            Uncreate(pi),
            Uncreate(f1),
        )
        linea_interseccion.remove_updater(mov_point)
        self.wait()


class Scene2_1(MovingCameraScene):
    def construct(self):
        rectangulos.set_fill(opacity=0)
        self.add(rectangulos, linea_guia)

        self.camera.frame.save_state()
        self.camera.frame.set(width=3.8).move_to(linea_guia)

        # funcion para mover punto linea guia
        global anguloTracker
        global end
        end = False

        self.play(Create(angulo), Write(f5), Create(angulo2), Write(f7))

        linea_guia.add_updater(mov_point_angle)

        self.play(linea_guia.animate.shift([0.1, 0, 0]))
        self.play(anguloTracker.animate.set_value(anguloTracker.get_value() - 30))
        self.play(anguloTracker.animate.set_value(anguloTracker.get_value() + 89.99999))
        self.play(anguloTracker.animate.set_value(anguloTracker.get_value() - 59.99999))
        self.play(Write(f6))
        self.play(linea_guia.animate.shift([-0.1, 0, 0]))
        end = True
        alpha = (
            MathTex(r"\alpha")
            .next_to(
                (
                    Angle(
                        linea_guia,
                        Line(Dot([x + 0.1, 0, 0]), Dot([x + 0.1, -1, 0])),
                        quadrant=(1, -1),
                        radius=0.08,
                        stroke_width=1,
                        color=BLUE,
                    )
                ),
                UP,
                buff=-0.06,
            )
            .shift([0.05, 0, 0])
            .scale(0.2)
        )

        linea_guia.remove_updater(mov_point_angle)
        self.play(
            FadeOut(angulo2),
            Uncreate(f7),
            f5.animate.become(alpha),
            angulo.animate.become(
                Angle(
                    linea_guia,
                    Line(Dot([x + 0.1, 0, 0]), Dot([x + 0.1, -1, 0])),
                    quadrant=(1, -1),
                    radius=0.08,
                    stroke_width=1,
                    color=BLUE,
                )
            ),
        ),
        f1 = MathTex(r"x").scale(0.2).next_to(linea_interseccion, UP, buff=0.035)
        f2.next_to(
            (
                MathTex(r"0\leqslant \alpha \leqslant \frac{\pi}{2}")
                .scale(0.28)
                .next_to(f1, RIGHT, buff=0.7)
                .shift([0.4, 0.5, 0])
            ),
            DOWN,
            buff=0.09,
        )

        self.wait()
        linea_interseccion.add_updater(mov_point)
        
        self.play(Create(pi), Create(centro), Create(linea_interseccion), Write(f1))

        self.play(
            f6.animate.become(
                MathTex(r"0\leqslant \alpha \leqslant \frac{\pi}{2}")
                .scale(0.28)
                .next_to(f1, RIGHT, buff=0.7)
                .shift([0.4, 0.5, 0])
            ),
            Write(f2),
        )
        f2.add(f6)
        rect = SurroundingRectangle(f2, TEAL, stroke_width=1).scale(0.9)
        self.play(Create(rect))
        self.wait()
        self.play(Uncreate(rect), Uncreate(f2), Uncreate(f6))

        self.wait()


class Scene2_3(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.camera.frame.set(width=3.8).move_to(linea_guia)
        rectangulos.set_fill(opacity=0)

        # radio de los angulos
        global radio
        global f5
        global f1
        global buff
        radio = 0.08

        # angulo alpha
        angulo.become(
            Angle(
                linea_guia,
                Line(Dot([x + 0.1, 0, 0]), Dot([x + 0.1, -1, 0])),
                quadrant=(1, -1),
                radius=radio,
                stroke_width=1,
                color=BLUE,
            )
        )
        # simbolo para alpha

        alpha = (
            MathTex(r"\alpha")
            .next_to(angulo, UP, buff=-0.06)
            .shift([0.05, 0, 0])
            .scale(0.2)
        )

        # simbolo para x

        buff = 0.035
        f1 = MathTex(r"x").scale(0.2).next_to(linea_interseccion, UP, buff=buff)

        # punto extra del triangulo
        pi_extra = Dot([linea_guia.get_all_points()[0][0], pi.get_y(), 0]).scale(0.2)

        # linea punteada
        dlinea1 = DashedLine(
            Dot(linea_guia.get_all_points()[0]).scale(0.01),
            pi_extra,
            dash_length=0.02,
            stroke_width=1,
            color=GREEN,
        )

        # segunda linea punteada
        dlinea2 = DashedLine(
            pi_extra, pi, dash_length=0.02, stroke_width=1, color=GREEN
        )

        # proporcion de brace
        n = 0.3
        brace1 = Brace(
            Line(pi_extra, centro, stroke_width=1).scale(n ** (-1)),
            sharpness=2.5,
            stroke_width=-0.5,
            direction=[0, 1, 0],
            buff=0.04,
        ).scale(n * 1.1)

        # acotacion para x
        acotacionX = (
            MathTex(r"0 \leqslant", "x", r"\leqslant", r"\sin{\alpha}\cdot \frac{k}{2}")
            .scale(0.2)
            .shift([2.05, 0.4, 0])
        )

        acotacion2X = (
            MathTex(r"\sin{\alpha}\cdot \frac{k}{2}", r"<", "x")
            .scale(0.2)
            .shift([2.05, 0.4, 0])
        )

        # texto del brace
        brace1Text = brace1.get_tex(r"\sin{\alpha}\cdot \frac{k}{2}", buff=-0.35).scale(
            0.2
        )

        # updater para punto
        def mov_point_triangle(obj):
            puntos = linea_guia.get_all_points()

            obj.move_to([puntos[0][0], centro.get_y(), 0])

            dlinea1.become(
                DashedLine(
                    Dot(linea_guia.get_all_points()[0]).scale(0.01),
                    pi_extra,
                    dash_length=0.02,
                    stroke_width=1,
                    color=GREEN,
                )
            )

            # segunda linea punteada
            dlinea2.become(
                DashedLine(pi_extra, pi, dash_length=0.02, stroke_width=1, color=GREEN)
            )
            alpha.become(
                MathTex(r"\alpha")
                .next_to(angulo, UP, buff=-0.06)
                .shift([0.05, 0, 0])
                .scale(0.2)
            )
            brace1.become(
                Brace(
                    Line(pi_extra, centro, stroke_width=1).scale(n ** (-1)),
                    sharpness=2.5,
                    stroke_width=-0.5,
                    direction=[0, 1, 0],
                    buff=0.04,
                ).scale(n * 1.1)
            )

            brace1Text.next_to(brace1, UP, buff=buff)

        # self.add(
        #     rectangulos,
        #     linea_guia,
        #     pi,
        #     centro,
        #     linea_interseccion,
        #     angulo,
        #     alpha,
        #     f1,
        #     dlinea1,
        #     pi_extra,
        #     dlinea2,
        #     brace1,
        #     brace1Text,
        # )

        self.add(rectangulos, linea_guia, angulo, alpha, f1, linea_interseccion,pi,centro)
    
        # se agrega updater
        linea_interseccion.add_updater(mov_point)

        linea_guia.add_updater(mov_point_angle)
        self.play(Create(pi_extra), Create(dlinea1), Create(dlinea2))
        pi_extra.add_updater(mov_point_triangle)
        self.play(Create(brace1), Write(brace1Text))

        self.play(
            anguloTracker.animate.set_value(79),
            run_time=1.5,
        )

        self.play(
            anguloTracker.animate.set_value(30),
            linea_guia.animate.shift([-0.1, 0, 0]),
            run_time=1.5,
        )
        self.play(
            anguloTracker.animate.set_value(anguloTracker.get_value() + 10),
            linea_guia.animate.shift([0.2, 0, 0]),
            run_time=1,
        )

        self.play(
            anguloTracker.animate.set_value(anguloTracker.get_value() - 10),
            linea_guia.animate.shift([-0.1, 0, 0]),
            run_time=1,
        )

        brace1TextCopy = brace1Text.copy()
        f1Copy = f1.copy()
        self.play(
            brace1TextCopy.animate.move_to(acotacionX[3]),
            f1Copy.animate.move_to(acotacionX[1]),
        )
        self.play(Write(acotacionX))
        self.remove(brace1TextCopy, f1Copy)
        linea_guia.remove_updater(mov_point_angle)
        pi_extra.remove_updater(mov_point_triangle)
        self.play(
            Uncreate(pi_extra),
            Uncreate(dlinea1),
            Uncreate(dlinea2),
            FadeOut(brace1),
            Uncreate(brace1Text),
            Uncreate(alpha),
            Uncreate(angulo),
            Uncreate(f1),
            Uncreate(acotacionX),
        )

        # self.wait()
        self.add(linea_interseccion, pi, centro)
        self.play(linea_guia.animate.shift([-0.85, 0, 0]))
        pi_extra2 = Dot([linea_guia.get_all_points()[-1][0], pi.get_y(), 0]).scale(0.2)

        dlinea3 = DashedLine(
            Dot(linea_guia.get_all_points()[-1]).scale(0.2),
            pi_extra2,
            dash_length=0.02,
            color=GREEN,
            stroke_width=1,
        )

        angulo3 = Angle(
            linea_guia,
            dlinea3,
            radius=0.09,
            quadrant=(-1, 1),
            color=TEAL,
            stroke_width=1,
        )
        alpha = MathTex(r"\alpha").scale(0.2)
        alpha.next_to(angulo3, DOWN, buff=0.02).shift([-0.03, 0, 0])
        brace2 = Brace(
            Line(pi, centro, stroke_width=1).scale(n ** (-1)),
            sharpness=2.5,
            stroke_width=-0.5,
            buff=0.11,
        ).scale(n * 1.1)

        brace2Text = brace2.get_tex(r"x", buff=-0.05).scale(0.2)
        brace1Text = brace1Text = MathTex(r"\sin{\alpha}\cdot \frac{k}{2}").scale(0.2)
        brace1Text.next_to(
            Line(centro, pi_extra2, stroke_width=1), DOWN, buff=0.015
        ).scale(0.9)

        self.play(FadeIn(brace2), Write(brace2Text))
        self.wait()
        self.play(Create(pi_extra2), Create(dlinea3), Create(angulo3), Write(alpha))

        self.play(Write(brace1Text))
        self.wait()

        brace1TextCopy = brace1Text.copy()
        brace2TextCopy = brace2Text.copy()
        self.play(
            brace1TextCopy.animate.move_to(acotacion2X[0]).scale(1 / 0.9),
            brace2TextCopy.animate.move_to(acotacion2X[2]),
        )
        self.play(Write(acotacion2X))
        self.wait()

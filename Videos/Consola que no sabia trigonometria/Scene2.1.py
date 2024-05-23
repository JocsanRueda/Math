from manim import *
import math
import numpy

# Creamos figuras y se seccionan con plano


class Scene2_1(MovingCameraScene):
    def construct(self):
        
        #delta time
        delta_time=1/int(self.camera.frame_rate)
     
        # cubo como personaje
        Cubo = Square(side_length=1, fill_opacity=1, fill_color=YELLOW, stroke_width=3)
        Cubo.set_stroke(color=GRAY)
        Cubo.scale(0.5).shift([2, 2, 0])

        # Ejes
        Ejes = Axes(x_range=[-7, 7, 1], y_range=[-7, 7, 1], x_length=12, y_length=12)

        # Joystick Virtual
        # Circulo externo
        # radio mayor
        rMayor = 1
        CircExt = Circle(radius=rMayor, color=WHITE).to_edge(DOWN + LEFT)
        # circulo externo del joystick
        rMenor = 0.5
        CircInt = Circle(radius=rMenor, color=BLUE)
        CircInt.set_fill(color=BLUE, opacity=0.98)

        CircInt.move_to(CircExt.get_center())
        # armado de Joystick
        Joystick = VGroup()
        Joystick.add(CircInt, CircExt)

        # tracker para valroes de posiciones
        angulo = ValueTracker(0)
        magnitud = ValueTracker(0)

        # -------------------------------- Triangulo de posicion 1-----------------------------------

        pt1_1 = Dot(ORIGIN)
        pt1_2 = Dot(Cubo.get_center())
        pt1_3 = Dot([Cubo.get_x(), 0, 0])

        # lienas del triangulo
        l1_1 = Line(pt1_1, pt1_2)
        l1_2 = Line(pt1_2, pt1_3)
        l1_3 = Line(pt1_3, pt1_1)

        l1_1.set_stroke(color=BLUE)
        l1_2.set_stroke(color=BLUE)
        l1_3.set_stroke(color=BLUE)

        anguloT1 = Angle(l1_3, l1_1, radius=0.5, quadrant=(-1, 1))
        textAnguloT1 = MathTex(r"\theta_0").next_to(anguloT1, UR, buff=0).scale(0.7)
        triangulo1 = VGroup()

        triangulo1.add(l1_1, l1_2, l1_3, anguloT1, textAnguloT1)

        # -------------------------------- Triangulo de posicion 2-----------------------------------

        pt2_1 = Dot(ORIGIN)
        pt2_2 = Dot(Cubo.get_center())
        pt2_3 = Dot([Cubo.get_x(), 0, 0])

        # lienas del triangulo
        l2_1 = Line(pt2_1, pt2_2)
        l2_2 = Line(pt2_2, pt2_3)
        l2_3 = Line(pt2_3, pt2_1)

        l1_1.set_stroke(color=BLUE)
        l1_2.set_stroke(color=BLUE)
        l1_3.set_stroke(color=BLUE)

        anguloT2 = Angle(l2_3, l2_1, radius=0.5, quadrant=(-1, 1))
        textAnguloT2 = MathTex(r"\theta_1").next_to(anguloT2, UR, buff=0).scale(0.7)
        triangulo2 = VGroup()

        triangulo2.add(l2_1, l2_2, l2_3, anguloT2, textAnguloT2)

        def mov_joystick(m):
            if magnitud.get_value() > 0:
                centro = m.get_center()
                centroExt = CircExt.get_center()

                x = math.cos(angulo.get_value()) * magnitud.get_value()
                y = math.sin(angulo.get_value()) * magnitud.get_value()

                if (
                    pow(x + centro[0] - centroExt[0], 2)
                    + pow(y + centro[1] - centroExt[1], 2)
                    <= rMayor
                ):
                    m.shift([x, y, 0])
                else:
                    newPoint = CircExt.point_at_angle(angulo.get_value())

                    m.move_to(newPoint)

        # Funcion que permite move el personaje al ajustar los tracker de angulo ymagnitud
        def mov_personaje(obj):

            if magnitud.get_value() > 0:
                x = math.cos(angulo.get_value()) * (magnitud.get_value())*delta_time
                y = math.sin(angulo.get_value()) * (magnitud.get_value())*delta_time
                Cubo.shift([x, y, 0])

        def updater_triangulo(obj):
            # obj.set_points(ORIGIN, Cubo.get_center(), [Cubo.get_x(), 0, 0])

            pt1_2.move_to(Cubo.get_center())
            pt1_3.move_to([Cubo.get_x(), 0, 0])
            l1_1.put_start_and_end_on(pt1_1.get_center(), pt1_2.get_center())
            l1_2.put_start_and_end_on(pt1_2.get_center(), pt1_3.get_center())
            l1_3.put_start_and_end_on(pt1_3.get_center(), pt1_1.get_center())
            anguloT1.become(Angle(l1_3, l1_1, radius=0.5, quadrant=(-1, 1)))
            textAnguloT1.next_to(anguloT1, UR, buff=0.02)

        def updater_triangulo2(obj):
            # obj.set_points(ORIGIN, Cubo.get_center(), [Cubo.get_x(), 0, 0])
            pt2_1.move_to(pt1_2.get_center())
            pt2_2.move_to(Cubo.get_center())
            pt2_3.move_to([Cubo.get_x(), pt1_2.get_y(), 0])
            l2_1.put_start_and_end_on(pt2_1.get_center(), pt2_2.get_center())
            l2_2.put_start_and_end_on(pt2_2.get_center(), pt2_3.get_center())
            l2_3.put_start_and_end_on(pt2_3.get_center(), pt2_1.get_center())
            anguloT2.become(Angle(l2_3, l2_1, radius=0.5, quadrant=(-1, 1)))
            textAnguloT2.next_to(anguloT2, UR, buff=0.02)

        # ------------------------------------------------Texto matematico----------------------------------------------------#
        f1 = (
            MathTex(r"\sin(\theta_1)=\frac{y_1-y_0}{L}")
            .move_to(UP * 5 + RIGHT * 7.2)
            .scale(0.8)
        )
        f2 = MathTex(r"\cos(\theta_1)=\frac{x_1-x_0}{L}").next_to(f1, DOWN).scale(0.8)
        f3 = (
            MathTex(r"x_1", "=", r"\cos(\theta_1)", "L", "+", "x_0")
            .scale(0.8)
            .move_to(f1.get_center())
        )
        f4 = (
            MathTex(r"y_1", "=", r"\sin(\theta_1)", "L", "+", "y_0")
            .scale(0.8)
            .move_to(f2.get_center())
        )

        f5 = (
            MathTex(r"x_n", "=", r"\cos(\theta_n)", "L", "+", "x_{n-1}")
            .scale(0.8)
            .move_to(f1.get_center())
        )
        f6 = (
            MathTex(r"y_n", "=", r"\sin(\theta_n)", "L", "+", "y_{n-1}")
            .scale(0.8)
            .move_to(f2.get_center())
        )
        x0 = f3[-1].copy()
        y0 = f4[-1].copy()
        x1 = f3[0].copy()
        y1 = f4[0].copy()
        CircInt.add_updater(mov_joystick)
        Cubo.add_updater(mov_personaje)
        triangulo1.add_updater(updater_triangulo)
        # agregar elementos a pantall

        self.add(Cubo, Ejes, Joystick)

        self.add(pt1_1, pt1_2, pt1_3, triangulo1)
        # animaciones
        Cubo.save_state()
        CircInt.save_state()

        # para x=2.598
        # y=1.5
        angulo.set_value(PI / 10)
        # mover hacia arriba
        self.play(magnitud.animate.set_value(3))
        self.wait()

        magnitud.set_value(-1)

        self.play(Restore(CircInt), run_time=0.1)

        triangulo1.remove_updater(updater_triangulo)

        # se muetra x_0 y y_0
        y0.next_to(triangulo1, RIGHT)
        x0.next_to(triangulo1, DOWN)
        self.add(y0, x0)

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(Cubo))

        # segundo movimiento
        angulo.set_value(PI / 3)
        magnitud.set_value(0.1)
        triangulo2.add_updater(updater_triangulo2)
        self.add(triangulo2)
        # mover hacia arriba
        self.play(magnitud.animate.set_value(4))
        self.wait()
        magnitud.set_value(0)
        # -------------Elementos temporales----------------------------------
        line1Temp = Line(Cubo.get_center(), [Cubo.get_x(), 0, 0])
        line2Temp = Line([Cubo.get_x(), 0, 0], ORIGIN)
        Bline1 = Brace(
            line1Temp, direction=line1Temp.copy().rotate(PI / 2).get_unit_vector()
        ).shift([0.2, 0, 0])
        Bline2 = Brace(line2Temp).shift([0, -0.1, 0])

        # posicionamiento de texto
        y1.next_to(Bline1, RIGHT)
        x1.next_to(Bline2, DOWN)
        self.play(FadeIn(Bline1), FadeIn(Bline2))
        self.wait()
        self.play(Write(x1), Write(y1))
        self.play(Write(f1), Write(f2))
        
        self.wait()
        self.play(TransformMatchingTex(f1, f3))
        self.play(TransformMatchingTex(f2, f4))
        self.wait()
        self.play(TransformMatchingTex(f3, f5))
        self.play(TransformMatchingTex(f4, f6))
        self.wait()

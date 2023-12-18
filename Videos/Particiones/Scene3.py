from manim import *

#Escena de p(200)
class Scene3(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve

        formula = MathTex("p(200)")
        numero2 = MathTex("p(200)=3,972,999,029,388")
        tiempo = Tex("125,982 años, 11 meses, 20 dias y 11 horas ")
        p1 = Dot(ORIGIN, fill_opacity=0)
        p2 = Dot(ORIGIN)
        p1.move_to(numero2, LEFT)
        p2.move_to(numero2, RIGHT)
        linea = Line(p1, p2)

        self.play(Write(formula))
        self.wait(1)
        self.play(
            TransformMatchingTex(formula, numero2),
            self.camera.frame.animate.scale(0.2).move_to(p1),
        )

        def update_movimiento(mob):
            mob.move_to(p1.get_center())

        self.camera.frame.add_updater(update_movimiento)
        self.play(MoveAlongPath(p1, linea, rate_func=linear), run_time=1.3)
        self.camera.frame.remove_updater(update_movimiento)

        self.wait()

        self.play(Restore(self.camera.frame))
        self.play(Uncreate(numero2), Write(tiempo))
        self.wait(2)
        self.play(Uncreate(tiempo))
        self.wait()
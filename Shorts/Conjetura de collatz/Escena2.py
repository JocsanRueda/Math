from manim import *
config.frame_width=9
config.frame_height=16
config.pixel_width=2160
config.pixel_height=3840
config.frame_rate=60
class Escena2_video2(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve

        numero1 = MathTex("2^{60}")
        numero2 = MathTex("1,152,921,504,606,846,976")
        p1 = Dot(ORIGIN,fill_opacity=0)
        p2 = Dot(ORIGIN)
        p1.move_to(numero2, LEFT)
        p2.move_to(numero2, RIGHT)
        linea = Line(p1, p2)

        self.play(Write(numero1))
        self.play(
            TransformMatchingTex(numero1, numero2),
            self.camera.frame.animate.scale(0.2).move_to(p1),
        )

        def update_movimiento(mob):
            mob.move_to(p1.get_center())

        self.camera.frame.add_updater(update_movimiento)
        self.play(MoveAlongPath(p1, linea, rate_func=linear),run_time=1.3)
        self.camera.frame.remove_updater(update_movimiento)

        self.wait()

        self.play(Restore(self.camera.frame))

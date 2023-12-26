from manim import *


# Escena que muestra la primera parte del video
class Scen0(Scene):
    def construct(self):
        variables = (
            VGroup(MathTex("A"), MathTex("R"), MathTex("r"), MathTex("d"))
            .arrange_submobjects()
            .shift(UP)
        )

        f1 = MathTex(r"4").scale(1.5)
        f2 = MathTex(r"4=1+1+1+1").scale(1.3).next_to(f1, DOWN).shift([0, 2, 0])
        f3 = MathTex(r"4=2+1+1").scale(1.3).next_to(f2, DOWN)
        f4 = MathTex(r"4=2+2").scale(1.3).next_to(f3, DOWN)
        f5 = MathTex(r"4=3+1").scale(1.3).next_to(f4, DOWN)
        f6 = MathTex(r"4=4").scale(1.3).next_to(f5, DOWN)
        f7 = MathTex(r"p(4)=5").scale(1.3).next_to(f6, DOWN)

        f8 = MathTex(r"p(n), n \in \mathbb{N}_0").scale(1.3)
        f9 = MathTex(r"p(n)=n \hspace{0.2cm},   0 \leq n \leq3")
        f10 = MathTex(r"p(n)=?")

        self.play(Write(f1))
        self.wait(2)
        self.play(Uncreate(f1))
        self.play(Write(f2))
        self.wait()
        self.play(Write(f3))
        self.wait()
        self.play(Write(f4))
        self.wait()
        self.play(Write(f5))
        self.wait()
        self.play(Write(f6))
        # se eliminan las particionwe
        self.wait()
        self.play(Write(f7))
        self.wait()
        self.play(
            Uncreate(f6),
            Uncreate(f5),
            Uncreate(f4),
            Uncreate(f3),
            Uncreate(f2),
            Uncreate(f1),
            Uncreate(f7)
        )
        self.wait()

        self.play(Write(f8))
        self.play(f8.animate.move_to(UP * 2))
        f9.scale(1.3).next_to(f8, DOWN, buff=1)
        f10.scale(1.3).next_to(f9, DOWN, buff=1)

        self.play(Write(f9))
        self.play(Write(f10))
        self.wait()
        self.play(
            Uncreate(f8),
            Uncreate(f9),
            Uncreate(f10)
        )
        self.wait(1)

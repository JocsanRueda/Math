from manim import *


# grupo de puntos
class Object_Dots(VGroup):
    def __init__(self, num_dots=3, color=BLUE, **kwargs):
        super().__init__(*[Dot(color=color) for _ in range(num_dots)], **kwargs)


# Escena que muestra la primera parte del video
class Scen1(Scene):
    def construct(self):
        variables = (
            VGroup(MathTex("A"), MathTex("R"), MathTex("r"), MathTex("d"))
            .arrange_submobjects()
            .shift(UP)
        )

        f2 = MathTex("1+1+1+1").scale(1.3).shift([0, 1, 0])
        f2Diagram = [
            (
                Object_Dots(num_dots=1, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f2, DOWN * 1)
            ),
            (
                Object_Dots(num_dots=1, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f2, DOWN * 2)
            ),
            (
                Object_Dots(num_dots=1, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f2, DOWN * 3)
            ),
            (
                Object_Dots(num_dots=1, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f2, DOWN * 4)
            ),
        ]
        f3 = MathTex("2+1+1").scale(1.3).shift([0, 1, 0])
        f3Diagram = [
            (
                Object_Dots(num_dots=1, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f3, DOWN * 1)
            ),
            (
                Object_Dots(num_dots=1, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f3, DOWN * 2)
            ),
            (
                Object_Dots(num_dots=2, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f3, DOWN * 3)
                .shift([f2Diagram[0].height * 0.82, 0, 0])
            ),
        ]
        f4 = MathTex("4=2+2").scale(1.3).shift([0, 1, 0])
        f4Diagram = [
            (
                Object_Dots(num_dots=2, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f4, DOWN * 1)
            ),
            (
                Object_Dots(num_dots=2, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f4, DOWN * 2)
            ),
        ]
        f5 = MathTex("4=3+1").scale(1.3).shift([0, 1, 0])
        f5Diagram = [
            (
                Object_Dots(num_dots=1, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f5, DOWN * 1)
            ),
            (
                Object_Dots(num_dots=3, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f5, DOWN * 2)
                .shift([f2Diagram[0].height * 0.82 * 2, 0, 0])
            ),
        ]
        f6 = MathTex("4=4").scale(1.3).shift([0, 1, 0])
        f6Diagram = [
            (
                Object_Dots(num_dots=4, color=BLUE)
                .arrange(RIGHT, buff=0.1)
                .next_to(f6, DOWN * 1)
            )
        ]
        # puntos

        self.play(Write(f2))
        self.play(*[Create(obj) for obj in f2Diagram])
        self.wait(1)

        # se eliminan objectos en escena
        self.play(Uncreate(f2))
        self.play(*[Uncreate(obj) for obj in f2Diagram])

        self.play(Write(f3))
        self.play(*[Create(obj) for obj in f3Diagram])
        self.wait(1)
        # se eliminan objectos en escena
        self.play(Uncreate(f3))
        self.play(*[Uncreate(obj) for obj in f3Diagram])
        self.play(Write(f4))
        self.play(*[Create(obj) for obj in f4Diagram])
        self.wait(1)
        # se eliminan objectos en escena
        self.play(Uncreate(f4))
        self.play(*[Uncreate(obj) for obj in f4Diagram])
        self.play(Write(f5))
        self.play(*[Create(obj) for obj in f5Diagram])
        self.wait(1)
        # se eliminan objectos en escena
        self.play(Uncreate(f5))
        self.play(*[Uncreate(obj) for obj in f5Diagram])
        self.play(Write(f6))
        self.play(*[Create(obj) for obj in f6Diagram])
        self.wait(5)

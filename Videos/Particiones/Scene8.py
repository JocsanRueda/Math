from manim import *


class Scene8(Scene):
    def construct(self):
        # Definir variables

        # Definir fórmulas
        partitionForm1 = (
            MathTex(r"p(4)=(-1)\sum_{m=1}^{\infty }(-1)^m[p(4-w(m))+p(4-w(-m))]")
            .scale(0.69)
            .to_edge(UP)
        )
        partitionForm2 = (
            MathTex(
                r"p(4)=(-1) \left[(-1)^1[p(4 - w(1)) + p(4 - w(-1))] + (-1)^2[p(4 - w(2)) + p(4 - w(-2))] + \ldots\right]"
            )
            .scale(0.69)
            .next_to(partitionForm1, DOWN, buff=0.5)
            
        )
        partitionForm3 = (
            MathTex(
                r"p(4)=(-1) \left[(-1)^1[p(4 - 1) + p(4 - 2)] + (-1)^2[p(4 - 5) + p(4 - 7)] + \ldots\right]"
            )
            .scale(0.69)
            .next_to(partitionForm2, DOWN)
            
        )
        partitionForm4 = (
            MathTex(
                r"p(4)=(-1) \left[(-1)^1[p(3) + p(2)] + (-1)^2[p(-1) + p(-3)] + \ldots\right]"
            )
            .scale(0.69)
            .next_to(partitionForm3, DOWN)
            
        )
        partitionForm5 = (
            MathTex(
                r"p(4)=(-1) \left[(-1)^1[p(3) + p(2)] + (-1)^2[0 + 0] + \ldots\right]"
            )
            .scale(0.69)
            .next_to(partitionForm4, DOWN)
            
        )

        partitionForm6 = (
            MathTex(r"p(4)=(-1)[(-1)[p(3) + p(2)] + 0+\ldots\right]")
            .scale(0.69)
            .next_to(partitionForm5, DOWN)
            
        )
        partitionForm7 = (
            MathTex(r"p(4)=[p(3) + p(2)]")
            .scale(0.69)
            .next_to(partitionForm6, DOWN)
            
        )
        partitionForm8 = MathTex(r"p(4)=3 + 2").scale(0.69).next_to(partitionForm7, DOWN)
        partitionForm9 = MathTex(r"p(4)=5").scale(0.69).next_to(partitionForm8, DOWN)
        box = SurroundingRectangle(partitionForm9, color=BLUE)

        # Escribir la primera fórmula
        self.play(Write(partitionForm1))

        self.play(Write(partitionForm2))

        self.play(Write(partitionForm3))

        self.play(Write(partitionForm4))

        self.play(Write(partitionForm5))

        self.play(Write(partitionForm6))

        self.play(Write(partitionForm7))

        self.play(Write(partitionForm8))

        self.play(Write(partitionForm9))
        self.play(Create(box))

        self.wait()
        self.play(
            Uncreate(box),
            Uncreate(partitionForm9),
            Uncreate(partitionForm8),
            Uncreate(partitionForm7),
            Uncreate(partitionForm6),
            Uncreate(partitionForm5),
            Uncreate(partitionForm4),
            Uncreate(partitionForm3),
            Uncreate(partitionForm2),
            Uncreate(partitionForm1),
        )

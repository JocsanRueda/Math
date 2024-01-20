from manim import *


class MatchingFrac(Scene):
    def construct(self):
        variables = (
            VGroup(MathTex("a"), MathTex("b"), MathTex("c"))
            .arrange_submobjects()
            .shift(UP)
        )

        frac1 = MathTex(r"\frac{", "{{x}}", "}{", "{{y}}", " }", "=", "2")
        frac2 = MathTex(r"\frac{ {a} }{ {b} }", "=", "{{2}}")
        frac3 = MathTex(r"{{a}}", "=", "{{2}}", "{{b}}")

        self.add(frac1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(frac1, variables), frac2))
        self.wait(0.5)
        self.play(TransformMatchingTex(frac2, frac3))
        self.wait(0.5)

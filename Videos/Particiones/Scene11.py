from manim import *


class Scene11(Scene):
    def construct(self):
        form1 = MathTex(
            r"4=x_1+2x_2+3x_3+4x_4 \\ \\ \ x_1\le 4,x_2\le 2,x_3\le 1,x_4\le 1"
        )
        form2 = MathTex(r'n=x_1+2x_2+3x_3+\ldots .+nx_n')
        self.play(Write(form1))
        self.wait()
        self.play(Uncreate(form1))
        self.play(Create(form2))
        self.wait()

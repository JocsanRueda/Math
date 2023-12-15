from manim import *


class Scene11(Scene):
    def construct(self):
        form1 = MathTex(
            r"4=x_1+2x_2+3x_3+4x_4 \hspace{0.5cm}si \ x_1\le 4,x_2\le 2,x_3\le 1,x_4\le 1"
        ).move_to(UP)
        form2 = MathTex(r"n=x_1+2x_2+3x_3+\ldots .+nx_n  \\ si \hspace{0.2cm} x_i \leq \left\lfloor \frac{n}{i} \right\rfloor, (i=1,2,3,\dots,n)" )
        s1 = (
            MathTex(r"{x_1=0, x_2=0, x_3=0,x_4=1}")
            .next_to(form1, DOWN, buff=0.5)
            .set_color(BLUE)
        )
        s2 = MathTex(r"{x_1=0, x_2=2, x_3=0,x_4=0}").next_to(s1, DOWN).set_color(BLUE)
        s3 = MathTex(r"{x_1=1, x_2=0, x_3=1,x_4=0}").next_to(s2, DOWN).set_color(BLUE)
        s4 = MathTex(r"{x_1=2, x_2=1, x_3=0,x_4=0}").next_to(s3, DOWN).set_color(BLUE)
        s5 = MathTex(r"{x_1=4, x_2=0, x_3=0,x_4=0}").next_to(s4, DOWN).set_color(BLUE)
        self.play(Write(form1))
        self.play(Write(s1))
        self.play(Write(s2))
        self.play(Write(s3))
        self.play(Write(s4))
        self.play(Write(s5))
        self.wait()
        self.play(
            Uncreate(form1),
            Uncreate(s1),
            Uncreate(s2),
            Uncreate(s3),
            Uncreate(s4),
            Uncreate(s5),
        )
        self.play(Write(form2))
        self.wait()

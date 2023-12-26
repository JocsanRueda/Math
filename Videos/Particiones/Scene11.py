from manim import *


class Scene11(Scene):
    def construct(self):
        form1 = MathTex(
            r"4=x_1+2x_2+3x_3+4x_4 \hspace{0.5cm}si \ x_1\le 4,x_2\le 2,x_3\le 1,x_4\le 1"
        ).move_to(UP)
        form2 = MathTex(
            r"n=x_1+2x_2+3x_3+\ldots .+nx_n  \\ si \hspace{0.2cm} x_i \leq \left\lfloor \frac{n}{i} \right\rfloor \hspace{0.1cm} para \hspace{0.1cm} i=1,2,3,\dots,n"
        ).shift([0,1,0])
        s1 = (
            MathTex(r"1. \hspace{0.3cm}{x_1=0, x_2=0, x_3=0,x_4=1}")
            .next_to(form1, DOWN, buff=0.5)
            .set_color(BLUE)
        )
        s2 = MathTex(r"2. \hspace{0.3cm} {x_1=0, x_2=2, x_3=0,x_4=0}").next_to(s1, DOWN).set_color(BLUE)
        s3 = MathTex(r"3.\hspace{0.3cm} {x_1=1, x_2=0, x_3=1,x_4=0}").next_to(s2, DOWN).set_color(BLUE)
        s4 = MathTex(r"4.\hspace{0.3cm} {x_1=2, x_2=1, x_3=0,x_4=0}").next_to(s3, DOWN).set_color(BLUE)
        s5 = MathTex(r"5.\hspace{0.3cm} {x_1=4, x_2=0, x_3=0,x_4=0}").next_to(s4, DOWN).set_color(BLUE)
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
        text = form2[0][26:31].copy()
        self.play(Write(form2))
        self.play(text.animate.next_to(form2, DOWN,buff=0.9).scale(1.4).set_color(BLUE))
        self.wait()
        self.play(Uncreate(form2),Uncreate(text))
        self.wait()

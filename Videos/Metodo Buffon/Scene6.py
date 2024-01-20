from manim import *
import math


class Scene5(Scene):
    def construct(self):
        eq1 = MathTex(r"f_{_x}(x)", "=", "\\frac{ 2 }{ {{ d }} }").move_to(UP)

        eq2 = MathTex(r"f_{_\alpha}(\alpha)", "=", r"\frac{ 2 }{ {{ \pi }} }").next_to(
            eq1, DOWN
        )
        eq3 = MathTex(
            r"f_{_{x, \alpha }}(x,\alpha)",
            "=",
            r"f_{_x}(x)",
            r"\cdot",
            r"f_{_\alpha}(\alpha)",
        ).next_to(eq2, DOWN)

        eq3 = MathTex(
            r"f_{_{x, \alpha }}(x,\alpha)",
            "=",
            r"{{f_{_x}(x)}}",
            r"\cdot",
            r"{{f_{_\alpha}(\alpha)}}",
        ).next_to(eq2, DOWN)

        eq4 = MathTex(
            r"f_{_{x, \alpha }}(x,\alpha)",
            "=",
            r"\frac{2}{d}",
            r"\cdot",
            r"\frac{2}{\pi}",
        ).next_to(eq2, DOWN)
        eq5 = MathTex(
            r"f_{_{x, \alpha }}(x,\alpha)",
            "=",
            r"\frac{4}{d \pi}",
        ).next_to(eq2, DOWN)

        ac1 = MathTex(
            r"0 \leqslant x \leqslant \frac{k}{2} \sin {\alpha},\hspace{0.2cm} 0\leqslant \alpha \leqslant \frac{\pi}{2}"
        ).scale(0.7)

        

        eq6 = MathTex(
            r"p=\int_{0}^{\frac{\pi}{2}} \int_{0}^{\frac{k}{2} \sin{\alpha}} \frac{4} {d\pi} \cdot dx \hspace{0.05cm} d\alpha"
        ).scale(0.6)

        eq7 = MathTex(
            r"p=\frac{4} {d\pi} \cdot \int_{0}^{\frac{\pi}{2}} \int_{0}^{\frac{k}{2} \sin{\alpha}}   dx \hspace{0.05cm} d\alpha"
        ).scale(0.6)

        eq8 = MathTex(
            r"p=\frac{4} {d\pi} \cdot \int_{0}^{\frac{\pi}{2}} \left[ x \right]_{_0}^{^{\frac{k}{2} \sin{\alpha}}}    \hspace{0.05cm} d\alpha"
        ).scale(0.6)

        eq9 = MathTex(
            r"p=\frac{4} {d\pi} \cdot \int_{0}^{\frac{\pi}{2}} \frac{k}{2} \sin{\alpha}    \cdot d\alpha"
        ).scale(0.6)

        eq10 = MathTex(
            r"p=\frac{4} {d\pi} \cdot \frac{k}{2} \cdot \int_{0}^{\frac{\pi}{2}} \sin{\alpha}    \cdot d\alpha"
        ).scale(0.6)

        eq11 = MathTex(
            r"p=\frac{2k} {d \pi} \cdot \left[ -\cos{\alpha} \right]_{_0} ^{^ {\frac{\pi }{2} }}"
        ).scale(0.6)

        eq12 = MathTex(r"p=\frac{2k} {d \pi}").scale(0.6)

        self.play(Write(eq1), Write(eq2))
        self.play(Write(eq3))
        self.play(TransformMatchingTex(eq3, eq4))
        self.play(TransformMatchingTex(eq4, eq5))
        self.play(Uncreate(eq1), Uncreate(eq2))
        self.play(eq5.animate.move_to(UP))
        ac1.next_to(eq5,RIGHT)
        self.play(Write(ac1))
        eq5.to_edge(UP).shift([-2, 0, 0])
        eq6.to_edge(UP)
        eq7.next_to(eq6, DOWN)
        eq8.next_to(eq7, DOWN)
        eq9.next_to(eq8, DOWN)
        eq10.next_to(eq9, DOWN)
        eq11.next_to(eq10, DOWN)
        eq12.next_to(eq11, DOWN)
       
       
       

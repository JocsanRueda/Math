from manim import *
import math


class Scene6(Scene):
    def construct(self):
        eq1 = (
            MathTex(r"f_{_x}(x)", "=", "\\frac{ 2 }{ {{ d }} }").move_to(UP).scale(0.7)
        )

        eq2 = (
            MathTex(r"f_{_\alpha}(\alpha)", "=", r"\frac{ 2 }{ {{ \pi }} }")
            .next_to(eq1, DOWN)
            .scale(0.7)
        )
        eq3 = (
            MathTex(
                r"f_{_{x, \alpha }}(x,\alpha)",
                "=",
                r"f_{_x}(x)",
                r"\cdot",
                r"f_{_\alpha}(\alpha)",
            )
            .next_to(eq2, DOWN)
            .scale(0.7)
        )

        eq3 = (
            MathTex(
                r"f_{_{x, \alpha }}(x,\alpha)",
                "=",
                r"{{f_{_x}(x)}}",
                r"\cdot",
                r"{{f_{_\alpha}(\alpha)}}",
            )
            .next_to(eq2, DOWN)
            .scale(0.7)
        )

        eq4 = (
            MathTex(
                r"f_{_{x, \alpha }}(x,\alpha)",
                "=",
                r"\frac{2}{d}",
                r"\cdot",
                r"\frac{2}{\pi}",
            )
            .next_to(eq2, DOWN)
            .scale(0.7)
        )
        eq5 = (
            MathTex(
                r"f_{_{x, \alpha }}(x,\alpha)",
                "=",
                r"\frac{4}{d \pi}",
            )
            .next_to(eq2, DOWN)
            .scale(0.7)
        )

        ac1 = MathTex(
            r"0 \leqslant x \leqslant \frac{k}{2} \sin {\alpha}",
            r"\hspace{0.2cm} 0\leqslant \alpha \leqslant \frac{\pi}{2}",
        ).scale(0.7)

        eq6 = MathTex(
            r"p",
            r"=",
            r"\int",
            r"\int",
            r"\frac{4} {d\pi}",
            r"\cdot",
            r"dx",
            r"\hspace{0.05cm}",
            r"d\alpha",
        ).scale(0.6)

        eq6_2 = MathTex(
            r"p",
            r"=",
            r"\int_{0}^{\frac{\pi}{2}}",
            r"\int",
            r"\frac{4} {d\pi}",
            r"\cdot",
            r"dx",
            r"\hspace{0.05cm}",
            r"d\alpha",
        ).scale(0.6)

        eq6_3 = MathTex(
            r"p",
            r"=",
            r"\int_{0}^{\frac{\pi}{2}}",
            r" \int_{0}^{\frac{k}{2} \sin{\alpha}}",
            r"\frac{4} {d\pi}",
            r"\cdot",
            r"dx",
            r"\hspace{0.05cm}",
            r"d\alpha",
        ).scale(0.6)

        eq7 = MathTex(
            r"p",
            r"=",
            r"\frac{4} {d\pi}",
            r"\cdot",
            r"\int_{0}^{\frac{\pi}{2}}",
            r"\int_{0}^{\frac{k}{2} \sin{\alpha}}",
            r"\cdot",
            r"dx",
            r"\hspace{0.05cm}",
            r"d\alpha",
        ).scale(0.6)

        eq8 = MathTex(
            r"p",
            r"=",
            r"\frac{4} {d\pi}",
            r"\cdot",
            r"\int_{0}^{\frac{\pi}{2}}",
            r"\left[ x \right]_{_0}^{^{\frac{k}{2} \sin{\alpha}}}",
            r"\cdot",
            r"\hspace{0.05cm}",
            r"d\alpha",
        ).scale(0.6)

        eq9 = MathTex(
            r"p",
            r"=",
            r"\frac{4} {d\pi}",
            r"\cdot",
            r" \int_{0}^{\frac{\pi}{2}}",
            r"\frac{k}{2}",
            r"\sin{\alpha}",
            r"\cdot",
            r"d\alpha",
        ).scale(0.6)

        eq10 = MathTex(
            r"p",
            r"=",
            r"\frac{4} {d\pi}",
            r"\cdot",
            r"\frac{k}{2}",
            r"\cdot",
            r"\int_{0}^{\frac{\pi}{2}} \sin{\alpha}",
            r"\cdot d\alpha",
        ).scale(0.6)

        eq11 = MathTex(
            r"p",
            r"=",
            r"\frac{2k} {d \pi}",
            r"\cdot",
            r"\left[ -\cos{\alpha} \right]_{_0} ^{^ {\frac{\pi }{2} }}",
        ).scale(0.6)

        eq12 = MathTex(r"p", r"=", r"\frac{2k} {d \pi}").scale(0.6)
        eq13 = MathTex(r"k", r"=", r"d").scale(0.8)
        eq14 = MathTex(r"p", r"=", r"\frac{2} {\pi}").scale(0.6).scale(1.3)
        eq15 = (
            MathTex(
                r"p(A)",
                r"=",
                r"\frac{\text{Resultados Favorables}} {\text{Total de casos posibles}}",
            )
            .scale(0.6)
            .scale(1.3)
        )

        eq16 = (
            MathTex(
                r"p(A)",
                r"=",
                r"\frac{\text{Número de cortes}} {\text{Total de lanzamientos}}",
            )
            .scale(0.6)
            .scale(1.3)
        )

        eq17 = (
            MathTex(
                r"\frac{2k} {d \pi}",
                r"=",
                r"\frac{\text{Número de cortes}} {\text{Total de lanzamientos}}",
            )
            .scale(0.6)
            .scale(1.3)
        )

        
        eq18 = (
            MathTex(
                r"\pi",
                r"=",
                r"\frac{2\cdot k \cdot \text{Total de lanzamientos}} {d \cdot \text{Número de cortes}}",
            )
            .scale(0.6)
            .scale(1.3)
        )

        eq19 = (
            MathTex(
                r"\pi",
                r"=",
                r"\frac{2 \cdot \text{Total de lanzamientos}} { \text{Número de cortes}}",
            )
            .scale(0.6)
            .scale(1.3)
        )

        self.play(Write(eq1), Write(eq2))
        self.play(Write(eq3))
        self.play(TransformMatchingTex(eq3, eq4))
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait()
        self.play(Uncreate(eq1), Uncreate(eq2))
        self.play(eq5.animate.to_edge(UP))
        eq6.next_to(eq5, DOWN)
        self.play(Write(eq6))
        self.wait()
        self.play(Uncreate(eq5))
        self.play(eq6.animate.to_edge(UP))
        ac1.next_to(eq6, RIGHT, buff=0.3)
        self.play(Write(ac1[1]))
        eq6_2.move_to(eq6)
        eq6_3.move_to(eq6)
        eq7.next_to(eq6, DOWN)
        eq8.next_to(eq7, DOWN)
        eq9.next_to(eq8, DOWN)
        eq10.next_to(eq9, DOWN)
        eq11.next_to(eq10, DOWN)
        eq12.next_to(eq11, DOWN)
        self.play(TransformMatchingTex(eq6, eq6_2))
        self.wait()
        self.play(TransformMatchingTex(eq6_2, eq6_3))
        self.wait()
        self.play(TransformMatchingTex(eq6_3.copy(), eq7))
        self.wait()
        self.play(TransformMatchingTex(eq7.copy(), eq8))
        self.play(TransformMatchingTex(eq8.copy(), eq9))
        self.play(TransformMatchingTex(eq9.copy(), eq10))
        self.play(TransformMatchingTex(eq10.copy(), eq11))
        self.play(TransformMatchingTex(eq11.copy(), eq12))

        self.play(
            Uncreate(eq6_3),
            Uncreate(eq7),
            Uncreate(eq8),
            Uncreate(eq9),
            Uncreate(eq10),
            Uncreate(eq11),
            Uncreate(ac1[1]),
        )
        self.play(eq12.animate.to_edge(UP).scale(1.3))
        eq13.next_to(eq17, buff=0.8)

        self.play(Write(eq15))
        self.play(TransformMatchingTex(eq15, eq16))
        self.wait()
        self.play(TransformMatchingTex(eq16, eq17))
        self.play(TransformMatchingTex(eq17, eq18))
        self.wait()
        self.play(Write(eq13))
        self.play(TransformMatchingTex(eq18, eq19))

        self.wait()

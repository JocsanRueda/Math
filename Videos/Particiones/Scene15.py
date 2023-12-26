from manim import *

# Creamos figuras y se seccionan con plano


class Scene15_2(Scene):
    def construct(self):
        form = (
            MathTex(
                r"p(n) = \frac{1}{2\pi\sqrt{2}} \sum_{k \le \alpha\sqrt{n}} A_{k}(n) \sqrt{k} \frac{d}{dn} \Bigg\{\frac{e^{\frac{\pi}{k} \sqrt{\frac{2}{3}(n-1/24)}\,}}{\sqrt{n-1/24}} \Bigg\} + O\big(n^{-1/4}\big),"
            )
            .to_edge(UP)
            .scale(0.7)
        )
        form2 = (
            MathTex(
                r"A_{k}(n) = \sum_{\begin{smallmatrix}0 \le h < k\\ \operatorname{mcd}(h,k)=1\end{smallmatrix}}\omega_{h,k} \cdot e^{{-2\pi} i\frac{h}{k} n},"
            )
            .next_to(form, DOWN,buff=0.8)
            .scale(0.7)
        )
        form3 = (
            MathTex(
                r"\omega_{h,k} = e^{ \pi i \sum_{\mu=1}^{k-1} \frac{\mu}{k} \Big( \frac{h\mu}{k} – \Big[ \frac{h\mu}{k} \Big] – \frac{1}{2} \Big)} ,"
            )
            .next_to(form2, DOWN,buff=0.8)
            .scale(0.7)
        )

        form4 = MathTex(r"\alpha \in \mathbb{R}^+").next_to(form3,DOWN,buff=0.8).scale(0.6)

        self.play(Create(form),Create(form2),Create(form3),Create(form4))
        self.wait(1.5)
        


class Scene15(Scene):
    def construct(self):
        form = MathTex(
            r"P(n) = \frac{1}{2 \pi \sqrt{2}} \frac{d}{dn}\frac{e^{\pi \sqrt{\frac{2}{3} \left(n-\frac{1}{24}\right)}}}{\sqrt{n-\frac{1}{24}}}"
        )

        table = (
            MathTable(
                [
                    [20, 30, 40, 50, 60, 70],
                    [627, "5,604", "37,338", "204,226", "966,427", "4,087,968"],
                    [
                        "625.758 ",
                        "5,600.280 ",
                        "37,330.609",
                        "204,211.076",
                        "966,433.362",
                        "4,087,908.735",
                    ],
                    [0.2, 0.1, 0.020, 0.007, 0.001, 0.001],
                ],
                row_labels=[
                    MathTex("n"),
                    MathTex(r"p(n)"),
                    MathTex(r"P(n)"),
                    MathTex("Error \hspace{0.1cm}\%"),
                ],
                include_outer_lines=True,
                line_config={"stroke_width": 1.6, "color": TEAL},
            )
            .scale(0.54)
            .shift([0, -1.3, 0])
        )
        form_error = (
            MathTex(
                r"Error Relativo = \left| \frac{\text{Valor Verdadero} - \text{Valor Aproximado}}{\text{Valor Verdadero}} \right| \times 100\%"
            )
            .scale(0.7)
            .to_edge(DOWN)
        )

        self.play(Write(form))
        self.wait()
        self.play(form.animate.to_edge(UP))

        self.play(table.create())
        self.wait()

        # self.play(form.animate.to_edge(UP))
        # self.play(table.create())
        # self.play(Write(form_error))
        # self.wait()

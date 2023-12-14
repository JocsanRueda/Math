from manim import *

# Creamos figuras y se seccionan con plano


class Scene15(Scene):
    def construct(self):
        form = MathTex(
            r"p(n) = \frac{1}{2 \pi \sqrt{2}} \frac{d}{dn}\frac{e^{\pi \sqrt{\frac{2}{3} \left(n-\frac{1}{24}\right)}}}{\sqrt{n-\frac{1}{24}}}+ O\big(e^{k \sqrt{n}}\big)"
        )
        form2 = MathTex(r"p(n)= Q(n) + O\big(e^{k \sqrt{n}}\big)")

        form3 = MathTex(
            r"= \frac{1}{2 \pi \sqrt{2}} \frac{d}{dn}\frac{e^{\pi \sqrt{\frac{2}{3} \left(n-\frac{1}{24}\right)}}}{\sqrt{n-\frac{1}{24}}}"
        ).move_to(DOWN)

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
                    MathTex(r"Q(n)"),
                    MathTex("Error \%"),
                ],
                include_outer_lines=True,
                line_config={"stroke_width": 1.6, "color": TEAL},
            )
            .scale(0.55)
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

        self.play(form.animate.to_edge(UP))
        self.play(Write(form2))
        self.play(form2.animate.next_to(form, DOWN))
        form4 = form2[0][5:9].copy()

        self.play(form4.animate.move_to(DOWN).shift([-3, 0, 0]))
        form3.next_to(form4, RIGHT, buff=0.1)
        form4.add(form3)
        self.play(Write(form3))
        self.play(Uncreate(form), Uncreate(form2))
        self.play(form4.animate.to_edge(UP))
        self.play(table.create())
        self.wait()

        # self.play(form.animate.to_edge(UP))
        # self.play(table.create())
        # self.play(Write(form_error))
        # self.wait()

from manim import *

# Creamos figuras y se seccionan con plano


class Scene14(Scene):
    def construct(self):
        form = MathTex(
            r"p(n) \sim P(n) := \frac{1}{4n\sqrt{3}} e^{\pi \sqrt{ \frac{2}{3}n}}"
        )

        table = MathTable(
            [
                [20, 30, 40, 50, 60, 70],
                [627, "5,604", "37,338", "204,226", "966,427", "4,087,968"],
                [
                    "692.385",
                    "6,080.435",
                    "40,080.0805",
                    "217,590.499",
                    "1,024,004.484",
                    "4,312,669.963",
                ],
                [10.428, 8.502, 7.344, 6.544, 5.958, 5.497],
            ],
            row_labels=[
                MathTex("n"),
                MathTex(r"p(n)"),
                MathTex(r"P(n)"),
                MathTex("Error \%"),
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1.6, "color": TEAL},
        ).scale(0.55)
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
        self.play(Write(form_error))
        self.wait()

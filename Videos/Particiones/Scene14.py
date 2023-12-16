from manim import *




class Scene14(Scene):
    def construct(self):
        form = MathTex(
            r"p(n) \sim P(n) := \frac{1}{4n\sqrt{3}} e^{\pi \sqrt{ \frac{2}{3}n}}"
        )
        p1 = Dot([-3, 1, 0])
        p2 = Dot([2, 1, 0])
        p3 = Dot([1.5, 1, 0])
        linea1 = Line(p1.get_center(), p2.get_center(), color=BLUE).add(p1, p2)
        linea2 = Line(p1.get_center(), p3.get_center(), color=YELLOW).add(p3, p1.copy())

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
        form_error = MathTex(
            r"Error Relativo = \left| \frac{\text{Valor Verdadero} - \text{Valor Aproximado}}{\text{Valor Verdadero}} \right| \times 100\%"
        ).scale(0.7)

        self.play(Write(form_error))
        self.wait()
        self.play(Uncreate(form_error))
        self.play(Create(linea1))
        self.wait()
        self.play(Create(linea2))
        self.play(linea1.animate.shift([0, 1, 0]))
        brace1 = Brace(linea1, direction=UP)
        text1 = brace1.get_tex("5")
        Brace2 = Brace(linea2, direction=DOWN)
        text2 = Brace2.get_tex("4.5")
        self.play(FadeIn(brace1), FadeIn(Brace2), Write(text1), Write(text2))
        text3 = MathTex(
            r"Error=\left| \frac{\hspace{1.8cm}}{\hspace{1cm}} \right|  100\%"
        ).next_to(text2, DOWN, buff=0.8)
        textCopy = text1.copy()
        self.play(
            Write(text3),
            textCopy.animate.next_to(text3, UP, buff=-0.35).shift([-0.4, 0, 0]),
        )
        text4 = MathTex(r"-").next_to(textCopy, RIGHT)

        text2Copy = text2.copy()
        text1Copy = text1.copy()
        self.play(
            Write(text4),
            text2Copy.animate.next_to(text4, RIGHT),
            text1Copy.animate.next_to(text4, DOWN).shift([0.2, -0.2, 0]),
        )
        result = MathTex(r"Error=10\%").next_to(text3, DOWN).shift([-1.72, 0, 0])
        self.play(Write(result))
        self.wait()
        self.play(
            Uncreate(linea1),
            Uncreate(linea2),
            Uncreate(brace1),
            Uncreate(Brace2),
            Uncreate(text1),
            Uncreate(text2),
            Uncreate(text3),
            Uncreate(text4),
            Uncreate(textCopy),
            Uncreate(text1Copy),
            Uncreate(text2Copy),
            Uncreate(result),
        )

        self.play(Write(form))
        self.wait()

        self.play(form.animate.to_edge(UP))
        self.play(table.create())
        self.play(Write(form_error))

        self.wait()

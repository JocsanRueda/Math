from manim import *

# Creamos figuras y se seccionan con plano


class Scene16(Scene):
    def construct(self):
        form = MathTex(
            r"p(n)=\frac{1}{2\pi \sqrt{2}}\frac{d}{dn}(\frac{e^{\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})+\frac{(-1)^n}{2\pi }\frac{d}{dn}(\frac{e^{\frac{1}{2}\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})+\ldots      \\ +\ldots +\frac{\sqrt{3}}{\pi \sqrt{2}}\cos (\frac{2n\pi }{3}-\frac{\pi }{18})\frac{d}{dn}(\frac{e^{\frac{1}{3}\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})+O(e^{k\sqrt{n}})"
        ).scale(0.8)
        form2 = (
            MathTex(r"p(n)= Q(n) + O\big(e^{k \sqrt{n}}\big)")
            .next_to(form, DOWN)
            .scale(0.8)
        )

        form3 = (
            MathTex(
                r"=\frac{1}{2\pi \sqrt{2}}\frac{d}{dn}(\frac{e^{\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})+\frac{(-1)^n}{2\pi }\frac{d}{dn}(\frac{e^{\frac{1}{2}\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})+\ldots      \\ +\ldots +\frac{\sqrt{3}}{\pi \sqrt{2}}\cos (\frac{2n\pi }{3}-\frac{\pi }{18})\frac{d}{dn}(\frac{e^{\frac{1}{3}\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})"
            )
            .move_to(DOWN)
            .scale(0.8)
        )

        table = (
            MathTable(
                [
                    [20, 30, 40, 50, 60, 70],
                    [627, "5,604", "37,338", "204,226", "966,427", "4,087,968"],
                    [
                        "626.877",
                        "5,604.012",
                        "37,337.782",
                        "204,226.043",
                        "966,466.580",
                        "4,087,968.149",
                    ],
                    [
                        0.01961,
                        0.00021,
                        0.00058,
                        0.00002,
                        0.00409,
                        0.00000364,
                    ],
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

        self.play(Write(form))

        self.play(form.animate.to_edge(UP))
        self.play(Write(form2))
        self.play(Uncreate(form))
        self.play(form2.animate.to_edge(UP))
        form4 = form2[0][5:9].copy()

        self.play(form4.animate.move_to(DOWN).shift([-6, 0, 0]))
        form3.next_to(form4, RIGHT, buff=0.1).shift([0, -form3.height / 3.4, 0])
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

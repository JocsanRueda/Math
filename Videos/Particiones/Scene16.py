from manim import *

# Creamos figuras y se seccionan con plano


class Scene16(Scene):
    def construct(self):
        form = MathTex(
            r"P(n)=\frac{1}{2\pi \sqrt{2}}\frac{d}{dn}(\frac{e^{\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})+\frac{(-1)^n}{2\pi }\frac{d}{dn}(\frac{e^{\frac{1}{2}\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})+\frac{\sqrt{3}}{\pi \sqrt{2}}\cos (\frac{2n\pi }{3}-\frac{\pi }{18})\frac{d}{dn}(\frac{e^{\frac{1}{3}\pi \sqrt{\frac{2}{3}(n-\frac{1}{24})}}}{\sqrt{n-\frac{1}{24}}})"
        ).scale(0.6)
  
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
                    MathTex(r"P(n)"),
                    MathTex("Error\hspace{0.1cm} \%"),
                ],
                include_outer_lines=True,
                line_config={"stroke_width": 1.6, "color": TEAL},
            )
            .scale(0.54)
            
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

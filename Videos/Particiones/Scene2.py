from manim import *


class Scen1(Scene):
    def construct(self):
        table = MathTable(
            [
                [10, 42],
                [50, "204,226"],
                [100, "190,569,292"],
                [200, "3,972,999,029,388"],
                [1000, "24,061,467,864,032,622,473,692,149,727,991 "],
            ],
            col_labels=[MathTex('n'),MathTex('p(n)')],

            include_outer_lines=True,
        )
 
 
        self.play(table.create())
        self.wait(1)

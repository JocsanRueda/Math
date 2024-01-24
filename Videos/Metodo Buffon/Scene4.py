from manim import *
import math


class Scene4(Scene):
    def construct(self):
        f1 = MathTex(r"0\leqslant x \leqslant \frac{d}{2}").scale(0.7).to_edge(UP)
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [0]},
            tips=False,
        ).scale(0.8)

        labels = ax.get_axis_labels()

        fn1 = ax.plot(lambda x: 4, x_range=[0, 4], color=BLUE)
        line1 = ax.get_vertical_line(ax.input_to_graph_point(4, fn1), color=YELLOW)
        area1 = ax.get_area(fn1, [0, 4], color=GRAY, opacity=0.4)
        form1 = MathTex(r"\frac{d}{2}").scale(0.8).next_to(line1, DOWN, buff=0.3)
        form2 = MathTex(r"y").scale(0.8).next_to(area1, RIGHT, buff=0.3)
        form3 = MathTex(r"f_{_x}(x)").scale(0.8).next_to(area1, UP, buff=0.3)
        form4 = form2.copy()

        form6 = form1.copy()
        form7 = MathTex(r"=1").scale(0.8)

        eq1 = (
            MathTex(r"{{y}}", "\cdot", "\\frac { {d} }{2}", "=1")
            .scale(0.8)
            .to_edge(UP + RIGHT)
            .shift([-1, 0, 0])
        )
        eq2 = (
            MathTex(r"{{y}}", "=", "\\frac{ 2 }{ {{ d }} }")
            .scale(0.8)
            .to_edge(UP + RIGHT)
            .shift([-1, 0, 0])
        )
        eq3 = (
            MathTex(r"f_{_x}(x)", "=", "\\frac{ 2 }{ {{ d }} }")
            .scale(0.8)
            .to_edge(UP + RIGHT)
            .shift([-1, 0, 0])
        )
        #self.add(f1, fn1, ax, labels, form1, area1, line1, form2, form3)


        self.play(Create(ax), Create(labels))
        self.play(
            Create(fn1),
            Write(f1),
            Write(form1),
        )
        self.play(Create(line1),Create(area1))
        self.play(Write(form3))
        self.play(Write(form4))

        self.play(form4.animate.move_to(eq1[0][0]))
        form5 = eq1[1][0]
        self.play(Write(form5), form6.animate.move_to(eq1[2][0:3].get_center()))
        form7 = eq1[3][0:]
        self.play(Write(form7))
        self.add(eq1)
        self.remove(form4, form5, form6, form7)

        self.play(TransformMatchingTex(eq1, eq2))
        self.play(TransformMatchingTex(eq2, eq3))

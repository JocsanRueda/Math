from manim import *
import math


class Scene3(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": []},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(
            lambda x: (10 / np.sqrt(2 * np.pi)) * np.exp(-1 * (x - 2.5) ** 2),
            x_range=[0, 5],
            color=GREEN_C,
        )

        curve_2 = ax.plot(lambda x: 0, x_range=[0, 5], color=WHITE)

        line_1 = ax.get_vertical_line(
            ax.input_to_graph_point(1.5, curve_1), color=YELLOW
        )
        line_2 = ax.get_vertical_line(ax.i2gp(3.5, curve_1), color=YELLOW)

        a = MathTex("a").scale(0.8).next_to(line_1, DOWN, buff=0.4)
        b = MathTex("b").scale(0.8).next_to(line_2, DOWN, buff=0.4)
        f = MathTex("f_{_x } (x)").next_to(curve_1, UP).shift([3, 0, 0])
        area = ax.get_area(
            curve_2, [1.5, 3.5], bounded_graph=curve_1, color=GREEN, opacity=0.5
        )
        f2 = (
            MathTex("p(a \leqslant x \leqslant b)= \int_{a} ^ {b}f(x)\cdot dx")
            .to_edge(UP + RIGHT)
            .shift([0, -2, 0])
            .scale(0.7)
        )
        f3 = (
            MathTex("\int_{-\infty} ^ {+\infty}f(x)\cdot dx=1")
            .next_to(f2, DOWN)
            .scale(0.7)
        )
        f4 = MathTex(r"f_{_x}(x)\geqslant 0").next_to(f3, DOWN).scale(0.7)
        flecha = Arrow(
            start=f.get_center() + [-0.05, -0.25, 0], end=[1.4, 0, 0], stroke_width=3
        )

        elementos = VGroup(ax, labels, curve_1, line_1, line_2, area, a, b, f, flecha)
        form1 = MathTex(r"a\leqslant x \leqslant b").move_to(UP)
        form2 = MathTex(r"f_{_x } (x) ").next_to(form1, DOWN, buff=0.5)
        self.play(Write(form1), Write(form2))
        self.wait()
        self.play(Uncreate(form1), Uncreate(form2))
        self.play(Create(ax), Write(labels), Create(curve_1))
        self.play(Write(f), Create(flecha))

        line_1.set_opacity(0)
        line_2.set_opacity(0)
        a.set_opacity(0)
        b.set_opacity(0)
        area.set_opacity(0)
        self.play(elementos.animate.scale(0.6).to_edge(LEFT))
        self.remove(line_1, line_2, a, b, area)
        line_1.set_opacity(1)
        line_2.set_opacity(1)
        a.set_opacity(1)
        b.set_opacity(1)
        area.set_opacity(0.4)
        self.play(
            Write(f2), Create(line_1), Create(line_2), Write(a), Write(b), FadeIn(area)
        )
        self.play(Write(f3))
        self.play(Write(f4))

        self.wait()

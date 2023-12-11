from manim import *


# plano de graficos
class Scen4(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.4,
            }
        )

        cos_func = FunctionGraph(
            lambda t: np.cos(t),
            color=BLUE,
        )

        form_cos = MathTex("f(x)= cos(x)").next_to(cos_func, UP).shift([-2, 0, 0])
        tan_func = FunctionGraph(lambda t: np.tan(t), color=TEAL)
        form_tan = MathTex("f(x)=tan(x)")
        form_tan.move_to(form_cos.get_center()).shift([-1.5, 0, 0])

        lineal_func = FunctionGraph(lambda t: t, color=GREEN)
        form_lineal = MathTex("f(x)=x").move_to(form_cos.get_center())

        form_partiton = MathTex("p(n)=?").move_to(form_cos.get_center())

        self.add(number_plane)
        self.play(Create(cos_func), Write(form_cos))
        self.wait()
        self.play(Transform(form_cos, form_tan), Transform(cos_func, tan_func))
        self.wait()
        self.play(Transform(form_cos, form_lineal), Transform(cos_func, lineal_func))
        self.wait()
        self.play(Uncreate(form_cos), Uncreate(cos_func))
        self.play(Write(form_partiton))

        self.wait()

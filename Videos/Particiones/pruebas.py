from manim import *


# plano de graficos
class Scen4(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 2,
                "stroke_opacity": 0.4,
            },
            x_axis_config={"numbers_to_include": np.arange(-10, 10, 1)},
            y_axis_config={"numbers_to_include": np.arange(-10, 10, 1)},
        )

        cos_func = FunctionGraph(
            lambda t: np.cos(t),
            color=BLUE,
        )

        def smooth_tan_parametric(t):
            return np.array([t, np.tan(t), 0])

        t = 0.1

        tan_func = VGroup(
            ParametricFunction(
                smooth_tan_parametric, t_range=[(-5 * np.pi / 2)+t, (-3 * np.pi / 2) - t]
            ).set_color(TEAL),
            ParametricFunction(
                smooth_tan_parametric, t_range=[-3*np.pi / 2+t, -1*np.pi / 2 - t]
            ).set_color(TEAL),
            ParametricFunction(
                smooth_tan_parametric, t_range=[ -1*np.pi / 2 + t,np.pi / 2-t]
            ).set_color(TEAL),
            ParametricFunction(
                smooth_tan_parametric, t_range=[ np.pi / 2+t,3 * np.pi / 2-t]
            ).set_color(TEAL),
            ParametricFunction(
                smooth_tan_parametric, t_range=[  3*np.pi / 2+t,5 * np.pi / 2-t]
            ).set_color(TEAL)
        )

        form_cos = MathTex("f(x)= cos(x)").next_to(cos_func, UP).shift([-2, 0, 0])

        form_tan = MathTex("f(x)=tan(x)")
        form_tan.move_to(form_cos.get_center()).shift([-1.5, 0, 0])

        lineal_func = FunctionGraph(lambda t: t, color=GREEN)
        form_lineal = MathTex("f(x)=x").move_to(form_cos.get_center())

        form_partiton = MathTex("p(n)=?").move_to(form_cos.get_center())

        self.play(Create(number_plane))
        self.play(Create(cos_func), Write(form_cos))
        self.wait()
        self.play(Transform(form_cos, form_tan), Transform(cos_func, tan_func))
        self.wait()
        self.play(Transform(form_cos, form_lineal), Transform(cos_func, lineal_func))
        self.wait()
        self.play(Uncreate(form_cos), Uncreate(cos_func))
        self.play(Write(form_partiton))
        self.play(Uncreate(number_plane), form_partiton.animate.move_to(ORIGIN))

        self.wait()
        

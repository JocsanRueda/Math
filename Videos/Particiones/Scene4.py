from manim import *


# plano de graficos
class Scen4(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            }
        )

        cos_func = FunctionGraph(
            lambda t: np.cos(t),
            color=BLUE,
        )
        form_cos = MathTex("f(x)= cos(x)").next_to(cos_func, UP).shift([-2, 0, 0])
        self.add(number_plane)
        self.play(Create(cos_func), Write(form_cos))
        self.wait()

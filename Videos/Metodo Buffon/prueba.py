from manim import *


class MatchingFrac(Scene):
    def construct(self):
        x = Tex("hola")

        self.play((Create(x) if 1 == 1 else Create(Tex())))

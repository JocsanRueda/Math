from manim import *


# Escena de p(200)
class Scene_extra_inicio(Scene):
    def construct(self):
        # create the axes and the curve

        formula = MathTex(r" 1 , 2 , 3, 4 , 5 , 6, 7, 8, 9, 10, \dots").scale(1.5)

        self.play(Write(formula))
        self.wait()
        self.play(Uncreate(formula))

        self.wait()

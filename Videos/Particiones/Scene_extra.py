from manim import *

#Escena de p(200)
class Scene_extra_p27(Scene):
    def construct(self):
     

        # create the axes and the curve

        formula = MathTex("p(27)")
      

        self.play(Write(formula))
        self.wait()
        self.play(Uncreate(formula))
       
        self.wait()
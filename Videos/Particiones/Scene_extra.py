from manim import *

#Escena de p(200)
class Scene_extra_p15(Scene):
    def construct(self):
     

        # create the axes and the curve

        formula = MathTex("p(15)")
      

        self.play(Write(formula))
        self.play(Uncreate(formula))
       
        self.wait()
from manim import *
#Creamos figuras y se seccionan con plano
class Escen6(Scene):
        def construct(self):
          
            variables = VGroup(MathTex("V"),MathTex("R"),MathTex("h")).arrange_submobjects().shift(UP)
            f1=MathTex("\pi", "{{R}}^2","=","\pi", "{{d}}^2","+", "\pi", "{{r}}^2")
            f2=MathTex("{{V}}_{ci}","=","{{V}}_{co}","+","{{V}}_{se}")
            f3=MathTex("{{V}}_{ci}","-","{{V}}_{co}","=","{{V}}_{se}")
            f4=MathTex("\pi","{{R}}^2","{{h}}"," - ",r"\frac{1}{3}","\pi","{{R}}^2","{{h}}"," = ","{{V}}_{se}")
            f5=MathTex(r"\pi","{{R}}^2","{{h}}"," - ",r"\frac{1}{3}","\pi","{{R}}^2","{{h}}"," = ","{{V}}_{se}")
            f6=MathTex(r"\frac{3}{3}","\pi","{{R}}^2","{{h}}"," - ",r"\frac{1}{3}","\pi","{{R}}^2","{{h}}"," = ","{{V}}_{se}")
            f7=MathTex(r"\frac{1}{3}","(","3\pi","{{R}}^2","{{h}}"," - ","\pi","{{R}}^2","{{h}}",")"," = ","{{V}}_{se}")  
            f8=MathTex(r"\frac{1}{3}","(","2\pi","{{R}}^2","{{h}}",")"," = ","{{V}}_{se}")
            f9=MathTex(r"\frac{2}{3}","\pi","{{R}}^2","{{h}}"," = ","{{V}}_{se}")
            f10=MathTex(r"\frac{2}{3}","\pi","{{R}}^2","{{R}}"," = ","{{V}}_{se}")
            f11=MathTex(r"\frac{2}{3}","\pi","{{R}}^3"," = ","{{V}}_{se}")
            f12=MathTex("2 ",r"\frac{2}{3}","\pi","{{R}}^3"," = ","2","{{V}}_{se}")
            f13=MathTex(r"\frac{4}{3}","\pi","{{R}}^3"," = ","{{V}}_{e}")
            f1.move_to(UP)
            
            
            
           
           
            t=1.8
            d=1.2   
            self.play(Write(f1))
            self.wait(11)
            self.play(TransformMatchingTex(Group(f1,variables),f2),run_time=t)
            self.wait(9)
            self.play(TransformMatchingTex(f2,f3),run_time=t)
            self.wait(d)
            self.play(TransformMatchingTex(Group(f3,variables),f4),run_time=t)
            self.wait(d)
            self.play(TransformMatchingTex(f4,f5),run_time=t)
            self.wait(d)
            self.play(TransformMatchingTex(f5,f6),run_time=t)
            self.wait(d)
            self.play(TransformMatchingTex(f6,f7),run_time=t)
            self.wait(d)
            self.play(TransformMatchingTex(f7,f8),run_time=t)   
            self.wait(d)  
            self.play(TransformMatchingTex(f8,f9),run_time=t) 
            self.wait(d)      
            self.play(TransformMatchingTex(f9,f10),run_time=t) 
            self.wait(d)
            self.play(TransformMatchingTex(f10,f11),run_time=t) 
            self.wait(d) 
            self.play(TransformMatchingTex(f11,f12),run_time=t) 
            self.wait(13)
            self.play(TransformMatchingTex(f12,f13  ),run_time=t)  
            self.wait(14) 
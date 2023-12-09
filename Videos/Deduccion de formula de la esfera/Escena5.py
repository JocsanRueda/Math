
from manim import *
#Creamos figuras y se seccionan con plano
class Escena5(ThreeDScene):
        def construct(self):
    
            self.set_camera_orientation(phi=60 * DEGREES, theta=-70* DEGREES)
            #posicion elementos
            ejes=ThreeDAxes()
            cilindro=Cylinder(radius=1,height=2,direction=Z_AXIS,resolution=20).shift((0,0,1))
            cilindro.set_color(BLUE)
            cilindro.set_opacity(0.8)
            circulo=Circle(radius=1,color=BLUE)
            circulo.set_fill(opacity=0.7)
            circulo.set_opacity(0.5)
            variables = VGroup(MathTex("A"), MathTex("r"), MathTex("h"),MathTex("V")).arrange_submobjects().shift(UP)
            f1=MathTex("{{A}}","=","\pi","{{r}}^2")
            f2=MathTex("{{Ah}}","=","\pi","{{r}}^2","{{h}}")
            f3=MathTex("{{V}}","=","\pi","{{r}}^2","{{h}}")

            f1.to_edge(UP+RIGHT,buff=2.5)
            f1.shift((0,0,0.5))
            f1.shift((0,0,1.5))
            f2.next_to(f1,DOWN)
            f3.next_to(f2,DOWN)
            
            self.add_fixed_in_frame_mobjects(f1)
            self.add_fixed_in_frame_mobjects(f2)
            self.add_fixed_in_frame_mobjects(f3)
            self.remove(f1,f2,f3)
            

            self.add(ejes)
            self.begin_3dillusion_camera_rotation()
            self.play(Create(circulo),Write(f1))
            self.wait(3)
            self.play(Create(cilindro),circulo.animate.shift((0,0,1.8)),Write(f2),run_time=1.5)
            self.play(FadeIn(circulo),run_time=0.4)

            #self.play(TransformMatchingTex(Group(f1,variables),f2))
            #self.play(TransformMatchingTex(f2,f3))
           
           
            self.play(Write(f3))

            self.wait(4)
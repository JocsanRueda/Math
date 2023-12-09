from manim import *
#Creamos figuras y se seccionan con plano
class Escena0(ThreeDScene):
        def construct(self):
    
            self.set_camera_orientation(phi=60 * DEGREES, theta=-70* DEGREES)
            #posicion elementos
            pE=(-3,0,1)
            pC=(0,0,0.75)
            pCI=(3,0,1)
            pRE=(0,0,0.5)
            
       
            #Creacion ejes
            Ejes=ThreeDAxes()
             #resolucion
            r=30
            o=0.4
            #racion de cubo
            cubo=Cube(2,fill_color=GREEN)
            cilindro=Cylinder(1,resolution=r)
            cilindro.set_color(BLUE)
            cilindro.set_opacity(o)
            

           
            #Creacion esfera
            
            Esfera=Sphere(center=pC,radius=1.5,resolution=r)
            Esfera.set_color(RED_B)
            Esfera.set_opacity(o)
            f1=MathTex(r"V=L^3").scale(1.3)
            f2=MathTex(r"V=\pi r^2 h").scale(1.3)
            f3=MathTex(r"V=\frac{4}{3}\pi r^3").scale(1.3)
            f1.to_edge(UP+RIGHT,buff=2.2)
            f2.to_edge(UP+RIGHT,buff=2.2)
            f3.to_edge(UP+RIGHT,buff=2.2)
     
           
            
            self.add(Ejes)
            
            self.begin_3dillusion_camera_rotation()
            self.add_fixed_in_frame_mobjects(f1)
            self.play(Create(cubo),Write(f1))
            self.wait(20.5)
            self.add_fixed_in_frame_mobjects(f2)
            self.play(Transform(cubo,cilindro),FadeOut(f1),FadeIn(f2))
            self.wait(9)
            self.add_fixed_in_frame_mobjects(f3)
            self.play(Transform(cubo,Esfera),FadeOut(f2),FadeIn(f3))
            self.wait(25.5)
            
            self.remove(cilindro)
           
            

         
           
from manim import *
# Creamos figuras y se seccionan con plano


class Escena0_1(Scene):
    def construct(self):

        img1 = ImageMobject("Img/1.jpeg").scale(1.8)
        lentes=ImageMobject("Img/lentes.png").scale(1.8)
        rect=Rectangle(BLUE,img1.height*1.05,img1.width*1.05)
        img1.add(rect)
        img2=ImageMobject("Img/2.jpg").scale(1.8)
        

        img1.to_edge(UP,buff=0.5)   
        nombre=Text("Ἀρχιμήδης (Archimedes)").scale(0.7)
        fecha=Text("287 a.C. - 212 a.C.").scale(0.7)
        img2.move_to(img1.get_center())     
       

        lentes.to_edge(UP,buff=-2)
        lentes.set_z_index(10)
        self.add(img1)
        
       
        nombre.next_to(img1,DOWN,buff=1)
        fecha.next_to(nombre,DOWN)
        self.play(FadeIn(img1),Create(rect))
        self.play(Write(nombre))
        self.play(Write(fecha))
        self.play(lentes.animate.move_to(img1.get_center()),run_time=1.7)
        self.play(FadeIn(img2),run_time=1)
       

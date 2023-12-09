from manim import *
#Creamos figuras y se seccionan con plano

config.frame_width=9
config.frame_height=16
config.pixel_width=2160
config.pixel_height=3840
config.frame_rate=60


# config.frame_width=9
# config.frame_height=16
# config.pixel_width=540
# config.pixel_height=960
# config.frame_rate=30
class Escena1_video2(Scene):
  def construct(self):

    # Configura la resolución a 1920x1080
  

    img1 = ImageMobject("Collatz.jpg").scale(0.7)
   
    img1.move_to(UP*4.2)
    rect=Rectangle(BLUE,img1.height*1.05,img1.width*1.05)
    rect.move_to(img1.get_center())
    img1.add(rect)

    nombre=Text("Lothar Collatz (1910–1990)").scale(0.7)
    nombre.next_to(img1,DOWN)
    variables = VGroup(MathTex("n"),MathTex("C")).arrange_submobjects().shift(UP)
  
    texto=Text("Aplicando reiteradamente la función de Collatz C \n\n a un número cualquiera llegaremos al número 1").scale(0.52)
    f1=MathTex(r"{{n}}").scale(1.7)
    f2=MathTex(r"{{n}}/2").scale(1.7)
    f3=MathTex(r"3{{n}}").scale(1.7)
    f4=MathTex(r"3{{n}}+1").scale(1.7)
    f5=MathTex(r"C(n) = \begin{cases} n/2, & \text{si } n \ es \ par \\ 3n+1, & \text{si } n \ es \ impar \end{cases}")
    texto.next_to(f5,DOWN,buff=1)
  
    f6=MathTex(r" 26 \longrightarrow 13 \longrightarrow 40  \\\longrightarrow 20 \longrightarrow 10 \longrightarrow 5 \\\longrightarrow 16 \longrightarrow 8 \longrightarrow 4 \\\longrightarrow 2 \longrightarrow 1")

    self.play(FadeIn(img1),Create(rect),Write(nombre))
    self.wait()
    self.play(Write(f5) )
    self.play(Write(texto))
    self.wait()
    self.play(
      FadeOut(img1),
      FadeOut(rect),
      FadeOut(nombre),
      FadeOut(texto)
    )
    self.play(FadeOut(f5))
    self.play(Write(f1))
    self.play(TransformMatchingTex(f1,f2))
    self.play(TransformMatchingTex(f2,f1))
    self.play(TransformMatchingTex(f1,f3))
    self.play(TransformMatchingTex(f3,f4))
    self.play(FadeOut(f4),Write(f5),Write(texto))
    self.play(FadeOut(f5),FadeOut(texto))
    self.play(Write(f6))
    self.wait()
    
  

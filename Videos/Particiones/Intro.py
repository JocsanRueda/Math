from manim import *

class MatEsl(Scene):
    def construct(self):
        # Crea el texto
        text = Text("MathEsl").scale(2)
        text2=Text("Mt").scale(2)
        # Agrega el texto a la pantalla
        self.add(text)

        # Crea el triángulo
        triangle = Triangle().scale(0.5)
        triangle.set_stroke(width=8)
        
        triangle.next_to(text[-1], RIGHT)
        triangle.rotate(PI)
        self.play(Write(text))
        # Hace que el triángulo caiga al lado del último carácter
        self.play(Create(triangle))
        self.play(Transform(text,text2),
        triangle.animate.next_to(text2[-1],RIGHT))
        

        self.wait(1)
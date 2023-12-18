from manim import *

# Creamos figuras y se seccionan con plano


class Scene17(Scene):
    def construct(self):
        # Configura la resolución a 1920x1080

   

        rect = Rectangle(BLUE,3.5,8).scale(1.6)


        nombre = Text("El hombre que conocia el infinito").scale(0.7)
        nombre.next_to(rect, DOWN)
 

        self.play( Create(rect), Write(nombre))
        self.wait()

        self.wait()
        self.play(Uncreate(rect), FadeOut(nombre))

        self.wait()

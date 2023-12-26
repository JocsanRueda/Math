from manim import *

# Creamos figuras y se seccionan con plano


class Scene12(Scene):
    def construct(self):
        # Configura la resolución a 1920x1080

        img1 = ImageMobject("assets/Srinivasa_Ramanujan.jpg").scale(0.4)

        rect = Rectangle(BLUE, img1.height * 1.06, img1.width * 1.06)
        rect.move_to(img1.get_center())
        img1.add(rect)

        nombre = Text("Srinivasa Ramanujan (1887–1920)").scale(0.7)
        nombre.next_to(img1, DOWN)
 

        self.play(FadeIn(img1), Create(rect), Write(nombre))
        self.wait()

        self.wait()
        self.play(FadeOut(img1), FadeOut(rect), FadeOut(nombre))

        self.wait()

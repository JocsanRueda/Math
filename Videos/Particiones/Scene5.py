from manim import *

# Creamos figuras y se seccionan con plano


class Scene5(Scene):
    def construct(self):
        # Configura la resolución a 1920x1080

        img1 = ImageMobject("assets/Leonhard_Euler.jpg").scale(0.7)

        rect = Rectangle(TEAL, img1.height * 1.06, img1.width * 1.06)
        rect.move_to(img1.get_center())
        img1.add(rect)

        nombre = Text("Leonhard Euler (1707–1783)").scale(0.7)
        nombre.next_to(img1, DOWN)
 

        self.play(FadeIn(img1), Create(rect), Write(nombre))
        self.wait()

        self.wait()
        self.play(FadeOut(img1), FadeOut(rect), FadeOut(nombre))

        self.wait()

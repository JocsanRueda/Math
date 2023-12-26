from manim import *

# Creamos figuras y se seccionan con plano


class Scene17(Scene):
    def construct(self):
        # Configura la resolución a 1920x1080

        img1 = ImageMobject("assets/portada.jpg").scale(0.5).shift([0, 0.5, 0])

        rect = Rectangle(BLUE, img1.height * 1.06, img1.width * 1.06)
        rect.move_to(img1.get_center())

        rect.set_stroke(width=2)

        img2 = ImageMobject("assets/frame0.png").scale(0.8).shift([0, 0.5, 0])

        rect2 = Rectangle(BLUE, img2.height * 1.06, img2.width * 1.06)
        rect2.move_to(img2.get_center())

        rect2.set_stroke(width=2)
        img3 = ImageMobject("assets/frame1.png").scale(0.8).shift([0, 0.5, 0])

        rect3 = Rectangle(BLUE, img3.height * 1.06, img3.width * 1.06)
        rect3.move_to(img3.get_center())

        rect3.set_stroke(width=2)

        img4 = ImageMobject("assets/frame2.png").scale(0.8).shift([0, 0.5, 0])

        rect4 = Rectangle(BLUE, img4.height * 1.06, img4.width * 1.06)
        rect4.move_to(img4.get_center())

        rect4.set_stroke(width=2)

        nombre = Text("El hombre que conocía el infinito (2015)").scale(0.7)
        nombre.next_to(img1, DOWN, buff=0.6)
        self.wait(0.5)
        self.play(FadeIn(img1), Create(rect), Write(nombre))
        self.wait()

        self.play(FadeOut(img1))
        self.play(FadeIn(img2), Transform(rect, rect2),nombre.animate.next_to(img2,DOWN,buff=0.6))
        self.wait()
        self.play(FadeOut(img2), FadeIn(img3), Transform(rect2, rect3))
        self.wait()
        self.play(FadeOut(img3), FadeIn(img4), Transform(rect3, rect4))


        self.wait()

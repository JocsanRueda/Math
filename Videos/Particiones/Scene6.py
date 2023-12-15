from manim import *

# Creamos figuras y se seccionan con plano


# Formula iterativa para particiones
class Scene6(Scene):
    def construct(self):
        # Configura la resolución a 1920x1080

        partitionForm = MathTex(
            r"p(n)=(-1)\sum_{m=1}^{\infty }(-1)^m[p(n-w(m))+p(n-w(-m))] ,"
        ).move_to(UP)

        wForm = MathTex(r"w(m)=\frac{m}{2}(3m-1), m\geq 1").next_to(partitionForm, DOWN)

        sigmaFunction = MathTex(
            r"\sum _{m=1}^{\infty }f(m)=f(1)+f(2)+f(3)+f(4)+\ldots"
        ).move_to(DOWN)

        # Crear formula de particion
        self.play(Write(partitionForm))
        self.play(Write(wForm))
        self.wait()
        self.play(
            partitionForm.animate.move_to(UP * 3.2), wForm.animate.move_to(UP * 1.7)
        )
        color_range = partitionForm[0][9:14]
        sigma = color_range.copy()
        self.play(color_range.animate.set_color(BLUE), sigma.animate.move_to(DOWN))
        self.play(sigma.animate.scale(1.5))

        self.wait()
        # Crear simbolo de
        self.play(Uncreate(sigma))
        self.play(Write(sigmaFunction))
        self.wait()
        self.play(Uncreate(sigmaFunction), color_range.animate.set_color(WHITE))
        self.wait()

        self.play(wForm.animate.move_to(ORIGIN))
        self.wait()

        self.play(Uncreate(wForm),Uncreate(partitionForm))
        self.wait()

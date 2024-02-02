from manim import *


# Creamos figuras y se seccionan con plano
class Scene0(Scene):
    def construct(self):
        circulo = Circle(radius=1, color=BLUE)
        circulo.set_fill(color=BLUE)
        linea = Line(ORIGIN, [2 * PI, 0, 0], color=BLUE).move_to(ORIGIN)

        pc = Dot(circulo.point_at_angle(PI))

        pe = Dot(circulo.point_at_angle(0))
        radio = Line(pc, pe)
        r = MathTex("d")
        l = MathTex("l").next_to(linea, UP)
        form = MathTex(r"\frac{ \hspace{0.5cm} }{\hspace{0.5cm}}").next_to(linea, RIGHT)
        form2 = MathTex(r" \frac{ \pi^2 }{6} = \sum_{n=1}^{\infty} \frac{1}{n^2}")
        r.next_to(radio, UP)

        formpi = MathTex(
            r" \pi \approx 3.141592653589793238462643383279502884197 \dots"
        ).scale(1.1)

        self.play(Write(formpi))
        self.wait()
        self.play(Uncreate(formpi))
        self.play(Create(circulo), Create(pc), Create(pe), Create(radio), Write(r))

        def line_updater(obj):
            obj.put_start_and_end_on(pc.get_center(), pe.get_center())

        def r_updater(obj):
            obj.next_to(radio, UP)

        radio.add_updater(line_updater)
        r.add_updater(r_updater)

        self.wait()
        self.play(
            Transform(circulo, linea),
            pc.animate.shift([0, -1, 0]),
            pe.animate.shift([0, -1, 0]),
        )

        self.play(Write(l), Uncreate(pc), Uncreate(pe))
        radio.remove_updater(line_updater)
        r.remove_updater(r_updater)
        lcopy = l.copy()
        rcopy = r.copy()
        self.play(
            Write(form),
            lcopy.animate.next_to(form, UP, buff=0.1),
            rcopy.animate.next_to(form, DOWN, buff=0.1),
        )
        self.wait()
        self.play(
            Uncreate(l),
            Uncreate(r),
            Uncreate(radio),
            Uncreate(circulo),
            Uncreate(form),
            Uncreate(rcopy),
            Uncreate(lcopy),
        )

        self.play(Write(form2))
        self.wait()

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

        formp1 = MathTex(
            r"\pi = 4 \left(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \ldots \right)"
        ).scale(0.7).to_edge(UP)

        # 2. Fórmula de Wallis

        formp2 = (
            MathTex(
                r"\pi = 4 \cdot \sum_{k=0}^{\infty} \frac{(-1)^k}{2k + 1}"
            )
           
            .next_to(formp1, DOWN)
            .scale(0.7)
        )

        # 3. Fórmula de Euler para π

        formp3 = (
            MathTex(r"\pi \approx \frac{1}{\frac{2\sqrt{2}}{9801} \sum_{k=0}^{\infty} \frac{(4k)! \cdot (1103 + 26390k)}{(k!)^4 \cdot 396^{4k}}}")
          
            .next_to(formp2, DOWN)
            .scale(0.7)
        )

       

        # 5. Fórmula de Ramanujan para π

        formp4 = (
            MathTex(
                r"\pi = \sqrt{6 \cdot \sum_{k=1}^{\infty} \frac{1}{k^2}}"
            )
           
            .next_to(formp3, DOWN)
            .scale(0.7)
        )

        # 6. Fórmula de Nilakantha Somayaji

        formp5 = (
            MathTex(r"\pi \approx \frac{426880 \sqrt{10005}}{\sum_{k=0}^{\infty} \frac{(6k)! \cdot (545140134k + 13591409)}{(3k)! \cdot (k!)^3 \cdot (-262537412640768000)^k}}")
          
            .next_to(formp4, DOWN)
            .scale(0.7)
        )

      
        self.play(
            Write(formp1), Write(formp2), Write(formp3), Write(formp4), Write(formp5)
        )
        self.wait()
        self.play(
            Uncreate(formp1),
            Uncreate(formp2),
            Uncreate(formp3),
            Uncreate(formp4),
            Uncreate(formp5)
        )
        self.wait()

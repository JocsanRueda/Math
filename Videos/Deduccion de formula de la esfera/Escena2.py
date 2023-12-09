from manim import *
# Creamos figuras y se seccionan con plano


class Escena2(MovingCameraScene):
    def construct(self):
        h = 0.5
        # Puntos iniciales
        pE = (-3, 1, 0)
        pC = (0, 0.5, 0)
        pCI = (2, 0.5, 0)
        pRE = (0, 0, 0.5)
        # Ejes
        Ejes = Axes(
            x_range=[-10, 10, 15],
            y_range=[-10, 10, 15],
            tips=True,
            axis_config={"include_numbers": False}
        )
        # Vertice Triangulo
        T_list = [
            (-1, 0, 0),
            (1, 0, 0),
            (0, 1, 0)
        ]
        T1_list = [
            (-1, 0, 0),
            (0, 0, 0),
            (0, 1, 0)
        ]

        # Triangulo
        triangulo = Polygon(*T_list)

        tr1 = Polygon(*T1_list)
        tr1.set_color(BLUE)

        # Puntos de linea
        p1 = (-5, 0.5, h)
        p2 = (4, 0.5, h)
        # Linea
        Rectangulo = Line(start=p1, end=p2)
        Rectangulo.set_color(BLUE)
        Rectangulo.set_stroke_width(2)
        tr1.set_stroke_width(2)
     

        # Esfera
        Esfera = Arc(radius=1, start_angle=0, angle=-PI)
        Esfera.move_to((-3, 0.5, 0))
        Esfera.set_color(RED)
        le = Line((-4.02, 1, 0), (-1.98, 1, 0))
        le.set_color(RED)
        # Cilindro

        Cilindro = Rectangle(color=GREEN, height=1, width=2)
        Cilindro.next_to(pCI)
        self.add(Rectangulo, Esfera, triangulo, Cilindro, le, Ejes)

         # Guardar estado
        self.camera.frame.save_state()

        # Escena Cono
        
        #self.play(self.camera.frame.animate.set(width=3.8).move_to(triangulo))
        #self.wait()
        self.camera.frame.set(width=3.8).move_to(triangulo)

        # puntos
        # Escena cono
        
        c1 = Dot(pC)  # cuspide
        c1.shift((0, 0.5, 0)).scale(0.5)
        c2 = Dot((0, 0.5, 0)).scale(0.5)  # centro
        c3 = Dot((-0.5, 0.5, 0)).scale(0.5)  # borde

        angulo = Square(0.1)
        angulo.set_color(BLUE)
        angulo.set_stroke(width=1.5)
        angulo.shift((-0.05, 0.05, 0))
        # linea
        linea2 = Line(start=c1, end=(0, 0, 0))
        linea2.set_color(BLUE)
        linea2.set_stroke_width(2)

        # subrayado de distancias
        subra1 = Brace(Line((-1, 0, 0), (0, 0, 0)), buff=0.05,
                       sharpness=1.5, stroke_width=0.0)
        subra2 = Brace(Line((0, 0, 0), (0, 1, 0)), buff=0.1, sharpness=0, stroke_width=1, direction=Line(
            (0, 0, 0), (0, 1, 0)).copy().rotate(-PI / 2).get_unit_vector())
        sb1 = subra1.get_text("R").scale(0.6)
        sb1.shift((0, 0.31, 0))
        sb2 = subra2.get_text("R").scale(0.6)
        d = Text("d").scale(0.4)
        d.next_to(Line(c1, c2), RIGHT, buff=0.1)
        d2 = Text("d").scale(0.4)
        d2.next_to(Line(c3, c2), DOWN, buff=0.1)
        Rectangulo.set_z_index(7)
        c1.set_z_index(8)
        c2.set_z_index(9)
        c3.set_z_index(10)
        subra1.set_z_index(11)
        subra2.set_z_index(12)
        sb1.set_z_index(13)
        sb2.set_z_index(14)
        self.play(Create(c1),
                  # Create(linea2),
                  Create(c2),
                  Create(c3),
                  )
        
        self.wait(6)

        self.play(Create(angulo))
        
        self.wait(14)
    # self.play(Uncreate(t2),Uncreate(t3))
        self.wait()

        # animacion 2
        self.play(
            DrawBorderThenFill(subra1),
            Write(sb1)
        )
        self.wait(1)
        self.play(
            
            DrawBorderThenFill(subra2),
            Write(sb2)
        )
        tr1.set_z_index(0)
        self.wait(2)
        self.play(
            Uncreate(subra1),
            Uncreate(subra2),
            Uncreate(sb1),
            Uncreate(sb2),
        )
        self.play(FadeOut(triangulo), FadeIn(tr1))
        self.wait(1)
       
        self.wait(4)
        self.play(Create(d))
        
        self.wait(12)
        self.play(Create(d2))
        self.wait(4)
        # self.add(d,d2,c1,c2,c3,linea2,angulo)
        # self.remove(t2,t3)
        # animacion 3

        def rec_updater(obj):
            obj.move_to((obj.get_x(), c3.get_y(), 0))

        def c2_updater(obj):
            obj.move_to((obj.get_x(), c3.get_y(), 0))

        def dc1_updater(obj):
            obj.next_to(Line(c1, c2), RIGHT, buff=0.1)

        def dc2_updater(obj):
            obj.next_to(Line(c3, c2), DOWN, buff=0.1)
        
        Rectangulo.add_updater(rec_updater)
        c2.add_updater(c2_updater)
        d.add_updater(dc1_updater)
        d2.add_updater(dc2_updater)
        p = c3.get_center()
        self.play(MoveAlongPath(c3, Line(c3, (-1, 0, 0))))
        self.play(MoveAlongPath(c3, Line((-1, 0, 0), p)))

        self.wait(2)
        self.play(Uncreate(d), Uncreate(d2), FadeOut(tr1), FadeIn(triangulo))

        Rectangulo.remove_updater(rec_updater)
        c2.remove_updater(c2_updater)
        d.remove_updater(dc1_updater)
        d2.remove_updater(dc2_updater)
        # Fin Escena Cono
        self.play(Restore(self.camera.frame))
        
        
        # Escena Esfera
        # self.play(self.camera.frame.animate.set(width=3.8).move_to(Esfera))
        # self.wait()   
        self.camera.frame.set(width=3.8).move_to(Esfera)
        # Angulo=Angle(Line((-0.1,0,0),(0.1,0,0)),Line((0,-0.1,0),(0,0.1,0)),radius=0.1,quadrant=(-1,1),other_angle=True,stroke_width=1.5)
        # Escena Esfera
        e1 = Dot((-3, 1, 0)).scale(0.5)  # Cuspide
        e2 = Dot((-3, 0.5, 0)).scale(0.5)  # centro
        e3 = Dot((-3.8660, 0.5, 0)).scale(0.5)
        e1.set_z_index(8)
        e2.set_z_index(9)
        e3.set_z_index(10)

        variables = VGroup(MathTex("R"), MathTex(
            "r"), MathTex("d")).arrange_submobjects().shift(UP)

        le1 = Line(e2, e1)  # centro-cuspide
        le2 = Line(e2, e3)  # centro-borde
        le3 = Line(e3, e1)  # borde-cuspide
        le2.set_z_index(8)
        de = MathTex("d").scale(0.4)
        r = MathTex("r").scale(0.4)
        de.next_to(le1, RIGHT, buff=0.1)
        r.next_to(le2, DOWN, buff=0.1)
        R = MathTex("R^2 = r^2+d^2")
        R.next_to(le3, UP, buff=-0.25).scale(0.4)
        R.rotate(30*DEGREES)
        self.wait(4)
        # Creacion puntos
        self.play(
            Create(e1),
            Create(e2),
            Create(e3)
        )
        # Creacion lineas
        self.wait(4)
        self.play(
            Create(le1))
        self.wait(4)
        self.play(Create(le2))
        self.wait(5)
        self.play(Create(le3))

        self.wait(4)
        self.play(
               Write(de))
        self.wait(5)
        self.play(Write(r))

           # self.add(e1,e2,e3,le1,le2,le3,de,r)

        def line1_updater(obj):
                obj.put_start_and_end_on(e1.get_center(), e2.get_center())

        def line2_updater(obj):
                obj.put_start_and_end_on(e2.get_center(), e3.get_center())

        def line3_updater(obj):
                obj.put_start_and_end_on(e3.get_center(), e1.get_center())

        def point_updater(obj):
                obj.move_to((-3, e3.get_y(), 0))

        def de_updater(obj):
                obj.next_to(le1, RIGHT, buff=0.1)

        def r_updater(obj):
                obj.next_to(le2, DOWN, buff=0.1)
        def rec2_updater(obj):
            obj.move_to((obj.get_x(), e3.get_y(), 0))

                
        Rectangulo.add_updater(rec2_updater)
        e2.add_updater(point_updater)
        le1.add_updater(line1_updater)
        le2.add_updater(line2_updater)
        le3.add_updater(line3_updater)
        de.add_updater(de_updater)
        r.add_updater(r_updater)
        arco = Arc(radius=1, start_angle=210*DEGREES, angle=60*DEGREES)
        arco2 = Arc(radius=1, start_angle=270*DEGREES, angle=-60*DEGREES)
        arco.move_to((-3.435, 0.25, 0))
        arco2.move_to((-3.435, 0.25, 0))

        self.play(MoveAlongPath(e3, arco))

        self.play(MoveAlongPath(e3, arco2))

        self.wait(7)
        self.play(Write(R))
        self.wait(2)
        self.play(
               Uncreate(le1),
               Uncreate(le2),
               Uncreate(le3),
               Uncreate(de),
               Uncreate(r),
               Uncreate(R),
               Uncreate(e1),
               Uncreate(e2),
               Uncreate(e3)
        )
        self.wait()

        e2.remove_updater(point_updater)
        le1.remove_updater(line1_updater)
        le2.remove_updater(line2_updater)
        le3.remove_updater(line3_updater)
        de.remove_updater(de_updater)
        r.remove_updater(r_updater)
        
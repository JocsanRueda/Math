from manim import *
class Escena1(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES)
        # posicion elementos
        pE = (-3, 0, 1)
        pC = (0, 0, 0.5)
        pCI = (3, 0, 0.5)
        pRE = (0, 0, 0.5)

        # Creacion ejes
        Ejes = ThreeDAxes()

        # resolucion
        r = 30
        o = 0.4
        # Creacion Semi_esfera
        Semi_esfera = Sphere(center=pE, radius=1,
                             resolution=r, v_range=(0, PI/2))
        Semi_esfera.set_color(RED_B)
        Semi_esfera.set_opacity(o)
        Esfera = Sphere(center=pE, radius=1, resolution=r)
        Esfera.set_color(RED_B)
        Esfera.set_opacity(o)
        Circulo=Circle(1)
        Circulo.set_color(RED_B)
        Circulo.set_opacity(o)
        Circulo.move_to(pE)
        # Creacion Cono
        Cono = Cone(base_radius=1, height=1, direction=Z_AXIS,
                    resolution=r, show_base=True)
        Cono.set_color(BLUE_B)
        Cono.move_to(pC)
        Cono.set_opacity(o)
        # Creacio Cilindro

        Cilindro = Cylinder(radius=1, height=1, direction=Z_AXIS, resolution=r)
        Cilindro.move_to(pCI)
        Cilindro.set_opacity(o)
        Cilindro.set_color(GREEN_B)

        #self.add(Semi_esfera, Cono, Cilindro, Ejes)

        # self.set_camera_orientation(phi=0,theta=-PI/2)

        # Creacion de rectangulo
        rectangulo = Rectangle(height=2.5, width=9,
                               color=BLUE, fill_opacity=0.5)
        rectangulo.move_to(pRE)
        rectangulo.rotate(PI)

 
        self.add(Circulo,Semi_esfera,Cono,Ejes)
        
        # creamos cilindo
        self.move_camera(frame_center=Cilindro, zoom=3.3)
        self.play(Create(Cilindro))
        self.wait(0.5)
        #self.set_camera_orientation(phi=60 * DEGREES, theta=-70* DEGREES)
        self.move_camera(frame_center=Ejes, zoom=1)
        

        self.begin_ambient_camera_rotation(rate=-PI/10, about="theta")

        self.wait(2)
        self.play(Create(rectangulo))

        self.wait(19)

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=60 * DEGREES, theta=-70 * DEGREES)
        # objetos de radio

        cs1 = Circle(radius=1, color=WHITE)
        cs2 = Circle(radius=1, color=WHITE)
        cs3 = Circle(radius=1, color=WHITE)
        cs1.move_to((-3, 0, 1))
        cs2.shift((0, 0, 1))
        cs3.move_to((3, 0, 1))

        pc1 = Dot3D(cs1.get_center()).scale(0.7)
        r1 = Dot3D(cs1.point_at_angle(PI)).scale(0.7)
        pc2 = Dot3D(cs2.get_center()).scale(0.7)
        r2 = pc2.copy()

        r = MathTex(r" r", font_size=30)
        dr = MathTex(r" d", font_size=30)

        slider = Dot((0, 0, 0)).set_opacity(0)

        radio1 = Line(r1, pc1)
        radio2 = Line((0,0,0), pc2)
        r.next_to(radio1, UP)
        dr.move_to(cs2.get_center())
        self.play(rectangulo.animate.move_to((0, 0, 1)))

        def cs1_udpater(obj):
            obj.move_to((obj.get_x(), obj.get_y(), 1-slider.get_z()))

        def cs2_udpater(obj):
            obj.move_to((obj.get_x(), obj.get_y(), 1-slider.get_z()))

        def cs3_udpater(obj):
            obj.move_to((obj.get_x(), obj.get_y(), 1-slider.get_z()))

        def r2_updater(obj):
            obj.move_to(cs2.point_at_angle(PI))

        def r1_updater(obj):
            obj.move_to(cs1.point_at_angle(PI))

        def radio1_updater(obj):
            obj.put_start_and_end_on(r1.get_center(), cs1.get_center())

        def radio2_updater(obj):
            obj.put_start_and_end_on(r2.get_center(), cs2.get_center())

        def r_updater(obj):
            obj.next_to(radio1, UP)

        def dr_updater(obj):
            obj.next_to(radio2, UP)

        def pc1_updater(obj):
            obj.move_to(cs1.get_center())

        def pc2_updater(obj):
            obj.move_to(cs2.get_center())

        def rectangulo_updater(obj):
            obj.move_to((obj.get_x(), obj.get_y(), 1-slider.get_z()))

        

        pc1.add_updater(pc1_updater)
        pc2.add_updater(pc2_updater)

        r2.add_updater(r2_updater)

        r1.add_updater(r1_updater)

        radio2.add_updater(radio2_updater)
        radio1.add_updater(radio1_updater)

        r.add_updater(r_updater)
        dr.add_updater(dr_updater)
        cs1.add_updater(cs1_udpater)
        cs2.add_updater(cs2_udpater)
        cs3.add_updater(cs3_udpater)
        rectangulo.add_updater(rectangulo_updater)
        self.add(cs3)
        h = 0.5

        self.play(
            GrowFromCenter(cs2),
            cs1.animate.scale(0.01),
            slider.animate.move_to((0, 0, 1)),
            run_time=2
        )

        cs1.scale(100)

        self.play(
            slider.animate.move_to((0, 0, 0)),
            cs2.animate.scale(0.01),
            GrowFromCenter(cs1),
            run_time=2
        )
        cs2.scale(100)

        self.play(
            GrowFromCenter(cs2),
            cs1.animate.scale(0.01),
            slider.animate.move_to((0, 0, 1)),
            run_time=2
        )

        cs1.scale(100)

        self.play(
            slider.animate.move_to((0, 0, 0)),
            cs2.animate.scale(0.01),
            GrowFromCenter(cs1),
            run_time=2
        )

        cs2.scale(100)
        self.play(
            GrowFromCenter(cs2),
            cs1.animate.scale(0.01),
            slider.animate.move_to((0, 0, 1)),
            run_time=2
        )

        cs1.scale(100)

        self.play(
            slider.animate.move_to((0, 0, 0)),
            cs2.animate.scale(0.01),
            GrowFromCenter(cs1),
            run_time=2
        )
        cs2.scale(100)

        self.play(
            FadeOut(cs1),
            FadeOut(cs2),
            FadeOut(cs3)
        )

        

        rectangulo.remove_updater(rectangulo_updater)

        pc1.remove_updater(pc1_updater)
        pc2.remove_updater(pc2_updater)

        r2.remove_updater(r2_updater)

        r1.remove_updater(r1_updater)

        radio2.remove_updater(radio2_updater)
        radio1.remove_updater(radio1_updater)

        r.remove_updater(r_updater)
        dr.remove_updater(dr_updater)
        cs1.remove_updater(cs1_udpater)
        cs2.remove_updater(cs2_udpater)
        cs3.remove_updater(cs3_udpater)

        self.play(
            rectangulo.animate.move_to((0, 0, h)),
            run_time=2
        )

        
        
        
        self.move_camera(phi=PI/2, theta=-PI/2)

        
        self.wait(2)

     
      
        self.move_camera(phi=PI/2, theta=-PI/2, frame_center=Cono, zoom=3.8)
        self.wait(2)
        self.move_camera(phi=0, theta=-PI/2)
        self.play(FadeOut(rectangulo),run_time=0.5)
        cs2.scale(0.6)
        self.play(FadeIn(cs2))
        self.wait(12)
        self.play(FadeOut(cs2))
        cs2.scale(1.666666667)
    
        self.move_camera(phi=0, theta=-PI/2)
        self.play(FadeIn(rectangulo),run_time=0.5)
        self.wait()
        
        self.move_camera(phi=PI/2, theta=-PI/2, frame_center=Ejes, zoom=1)
        self.move_camera(phi=PI/2, theta=-PI/2,
                         frame_center=Semi_esfera, zoom=3.8)
        self.wait(4)
        self.move_camera(phi=PI/2, theta=-PI/2, frame_center=Cono, zoom=1)
        self.wait()
        self.move_camera(phi=0, theta=-PI/2, frame_center=Ejes, zoom=1)
        self.wait(2)
        
        self.move_camera(phi=60 * DEGREES, theta=-70 * DEGREES)
        self.wait(2)
        
        # animaciones radio
        
        self.play(rectangulo.animate.move_to((0,0,1)))
        self.play(
            Create(cs1), 
            Create(pc1),
            Create(pc2), 
            Create(r1), 
            Create(radio1), 
            Write(r), 
            Write(dr), 
            Create(r2), 
            Create(radio2),
            Create(cs3))
        rectangulo.add_updater(rectangulo_updater)

        pc1.add_updater(pc1_updater)
        pc2.add_updater(pc2_updater)

        r2.add_updater(r2_updater)

        r1.add_updater(r1_updater)

        radio2.add_updater(radio2_updater)
        radio1.add_updater(radio1_updater)

        r.add_updater(r_updater)
        dr.add_updater(dr_updater)
        cs1.add_updater(cs1_udpater)
        cs2.add_updater(cs2_udpater)
        cs3.add_updater(cs3_udpater)

        
        self.play(
                GrowFromCenter(cs2),
                cs1.animate.scale(0.01),
                slider.animate.move_to((0,0,1)),
                run_time=2
                )
        
        cs1.scale(100)
        
        self.play(
                slider.animate.move_to((0,0,0)),
                cs2.animate.scale(0.01),
                GrowFromCenter(cs1),
                run_time=2 
            )
        
        cs2.scale(100)
        self.move_camera(phi=0, theta=-PI/2, frame_center=Ejes, zoom=1)
        self.wait()
        '''
        radio1.remove_updater(radio1_updater)
        radio2.remove_updater(radio2_updater)
        r2.remove_updater(r2_updater)

        r1.remove_updater(r1_updater)
        r.remove_updater(r_updater)
        dr.remove_updater(dr_updater)
        '''
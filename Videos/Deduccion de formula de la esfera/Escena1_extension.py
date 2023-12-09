from manim import *
# Creamos figuras y se seccionan con plano


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
        Circulo = Circle(1)
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

        self.begin_3dillusion_camera_rotation()
        self.play(Create(Ejes))
        # 24
        self.wait(24)

        self.stop_3dillusion_camera_rotation()

        centro = Dot3D(Esfera.get_center()).scale(0.7)
        borde = Dot3D((-4, 0, 1)).scale(0.7)
        radio = Line3D(centro, borde)
        radio.set_width(1)

        R = MathTex("R").scale(1.3)
        R.next_to(radio, UP,buff=0.08)
        R.shift((-0.105,0,0))
        self.add_fixed_orientation_mobjects(R)
        self.remove(R)

        # creamos Semi_esfera
        self.move_camera(frame_center=Semi_esfera, zoom=2.7)
        self.play(Create(Esfera))

        self.play(
            Create(centro),
            Create(borde),
            Create(radio),
            
        )
        self.play(Write(R))

        self.wait(1.5)
        self.play(
            Uncreate(centro),
            Uncreate(borde),
            Uncreate(radio),
            Uncreate(R)
        )

        self.play(Transform(Esfera, Semi_esfera))
        self.play(Create(Circulo))
        self.wait(0.5)
        # creamos Cono
        self.move_camera(frame_center=Cono, zoom=3.3)
        centro_cono = Dot3D((0, 0, 0)).scale(0.7)
        borde_cono = Dot3D((-1, 0, 0)).scale(0.7)
        cima = Dot3D((0, 0, 1)).scale(0.7)
        radio2 = Line3D(centro_cono, borde_cono)
        altura = Line3D(centro_cono, cima)
        R_Cono1 = MathTex("R").scale(1.3)
        R_Cono1.next_to(altura, RIGHT, buff=0.08)
        R_Cono2=R_Cono1.copy()
        R_Cono2.next_to(radio2, UP, buff=0.08)
        R_Cono2.shift((-0.109,0,0))
        

        self.add_fixed_orientation_mobjects(R_Cono1)
        self.add_fixed_orientation_mobjects(R_Cono2)
        self.remove(R_Cono1,R_Cono2)

        self.play(Create(Cono))

        self.play(
            Create(centro_cono),
            Create(borde_cono),
            Create(cima),
            Create(radio2),
            Create(altura)
        )
        self.play(
            Write(R_Cono1),
            Write(R_Cono2)
        )
        self.wait(1.5)
        self.play(

            Uncreate(centro_cono),
            Uncreate(borde_cono),
            Uncreate(cima),
            Uncreate(radio2),
            Uncreate(altura),
            Uncreate(R_Cono1),
            Uncreate(R_Cono2)
        )
        self.wait(0.5)
        # creamos cilindo
        self.move_camera(frame_center=Cilindro, zoom=3.3)

        centro_cilindro=Dot3D((3,0,0)).scale(0.7)
        borde_cilindro=Dot3D((2,0,0)).scale(0.7)
        cima_cilindro=Dot3D((3,0,1)).scale(0.7)
        radio_cilindro=Line3D(centro_cilindro,borde_cilindro)
        altura_cilindro=Line3D(centro_cilindro,cima_cilindro)
        R_cilindro=MathTex("R").scale(1.3)
        R_cilindro.next_to(altura_cilindro,RIGHT,buff=0.08)
        R_cilindro2=R_cilindro.copy()
        R_cilindro2.next_to(radio_cilindro,UP,buff=0.08)
        R_cilindro2.shift((-0.109,0,0))
      
        self.add_fixed_orientation_mobjects(R_cilindro)
        self.add_fixed_orientation_mobjects(R_cilindro2)
        self.remove(R_cilindro,R_cilindro2)

       


        

        self.play(Create(Cilindro))
        self.play(
            Create(centro_cilindro),
            Create(borde_cilindro),
            Create(cima_cilindro),
            Create(altura_cilindro),
            Create(radio_cilindro)
        )

        self.play(
            Write(R_cilindro),
            Write(R_cilindro2)
        )

        self.wait(1.5)
        self.play(
            Uncreate(centro_cilindro),
            Uncreate(borde_cilindro),
            Uncreate(cima_cilindro),
            Uncreate(altura_cilindro),
            Uncreate(radio_cilindro),   
            Uncreate(R_cilindro),
            Uncreate(R_cilindro2)
        )
        self.wait(2 )
        #self.set_camera_orientation(phi=60 * DEGREES, theta=-70* DEGREES)
        # self.wait()

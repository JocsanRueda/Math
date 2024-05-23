from manim import *
import math
import numpy

# Creamos figuras y se seccionan con plano


class Scene2(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES)
        delta_time=1/int(self.camera.frame_rate)
        # cubo como personaje
        Cubo = Cube(side_length=1, fill_opacity=1, fill_color=YELLOW, stroke_width=3)
        Cubo.set_stroke(color=GRAY)

        # Ejes
        Ejes = ThreeDAxes(x_range=[-7,7,1],y_range=[-7,7,1],x_length=12, y_length=12)
       
        # Joystick Virtual
        # Circulo externo
        # radio mayor
        rMayor = 1
        CircExt = Circle(radius=rMayor, color=WHITE).to_edge(DOWN + LEFT)
        # circulo externo del joystick
        rMenor = 0.5
        CircInt = Circle(radius=rMenor, color=BLUE)
        CircInt.set_fill(color=BLUE, opacity=0.98)

        CircInt.move_to(CircExt.get_center())
        # armado de Joystick
        Joystick = VGroup()
        Joystick.add(CircInt, CircExt)

        # tracker para valroes de posiciones
        angulo = ValueTracker(0)
        magnitud = ValueTracker(0)
        # animaciones

        def mov_joystick(m):
            centro = m.get_center()
            centroExt = CircExt.get_center()

            x = math.cos(angulo.get_value()) * magnitud.get_value()
            y = math.sin(angulo.get_value()) * magnitud.get_value()

            if (
                pow(x + centro[0] - centroExt[0], 2)
                + pow(y + centro[1] - centroExt[1], 2)
                <= rMayor
            ):
                m.shift([x, y, 0])
            else:
                newPoint = CircExt.point_at_angle(angulo.get_value())

                m.move_to(newPoint)

        # Funcion que permite move el personaje al ajustar los tracker de angulo ymagnitud
        def mov_personaje(obj):
            if magnitud.get_value() != 0:
                x = math.cos(angulo.get_value()) * (magnitud.get_value() )*delta_time
                y = math.sin(angulo.get_value()) * (magnitud.get_value() )*delta_time
                Cubo.shift([x, y, 0])

        # funcion que ajusta el texto P en funcion de la posicion del personaje
        def update_text(obj):
            (x,y,z) = Cubo.get_center()
            
            newP = MathTex(
                f"p=({ int(x) if x-int(x)==0 else round(x,2) },{ int(y)  if y-int(y)==0 else round(y,2)},{int(z) if z-int(z) ==0 else round(z,2)}  )"
            )
            newP.move_to(obj.get_center())
            
            
            obj.become(newP)
            self.add_fixed_in_frame_mobjects(obj)

        # ------------------------------------------------Texto magnematico----------------------------------------------------#
        # Tangente inversa
        f1 = MathTex(r"x=2.6").to_edge(UP + RIGHT).shift([-1, 0, 0])
        f2 = MathTex(r"y=2.6").next_to(f1, DOWN)
        f3 = MathTex(r"\theta= \tan^{-1}(\frac{y}{x})").next_to(f2, DOWN)
        f4 = MathTex(r"\theta \approx 0.5236").next_to(f2, DOWN)

        # cordenadas
        p = MathTex(r"p=(x_1,y_1,z_1)").to_edge(UP + RIGHT).shift([-1, 0, 0])
        p.add_updater(update_text)
        CircInt.add_updater(mov_joystick)
        Cubo.add_updater(mov_personaje)

        # agregar elementos a pantall

        self.add_fixed_in_frame_mobjects(Joystick)
        self.add(Cubo, Ejes)

        # self.play(Create(Joystick),Create(Cubo),Create(Ejes))

        # animaciones
        Cubo.save_state()
        Joystick.save_state()
        self.add_fixed_in_frame_mobjects(p)
        
        # # para x=2.598
        # #y=1.5
        angulo.set_value(PI / 6)
        #mover hacia arriba
        self.play(magnitud.animate.increment_value(8))
        self.wait()
        magnitud.set_value(0)
        p.remove_updater(update_text)
        self.play(Restore(Cubo),Restore(Joystick),Uncreate(p))
    
        ##-----------------------------Calculo de angulo---------------------------#

        self.add_fixed_in_frame_mobjects(f1)
        self.play(Write(f1))

        self.add_fixed_in_frame_mobjects(f2)

        self.play(Write(f2))

        self.add_fixed_in_frame_mobjects(f3)

        self.play(Write(f3))
        self.add_fixed_in_frame_mobjects(f4)
        f4.set_opacity(0)
        self.play(ReplacementTransform(f3, f4), f4.animate.set_opacity(1))
        self.play(Uncreate(f4),Uncreate(f3),Uncreate(f2),Uncreate(f1))
        # Mostrar posicion 
        self.move_camera(phi=0, theta=-PI/2, frame_center=Ejes, zoom=1)
        
        
        self.wait()

from manim import *
import math
import numpy

# Creamos figuras y se seccionan con plano


class Scene1(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES)
        delta_time=1/int(self.camera.frame_rate)
        # cubo como personaje
        Cubo = Cube(side_length=1, fill_opacity=1, fill_color=YELLOW, stroke_width=3)
        Cubo.set_stroke(color=GRAY)


        #ejes
        ejes=ThreeDAxes()
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
                
        def mov_personaje(obj):
            if(magnitud.get_value()!=0):
                x = math.cos(angulo.get_value()) * (magnitud.get_value())*delta_time
                y = math.sin(angulo.get_value()) * (magnitud.get_value())*delta_time
                Cubo.shift([x,y,0])
            


        
        CircInt.add_updater(mov_joystick)
        Cubo.add_updater(mov_personaje)
        
        #agregar elementos a pantall
        
        
        
        #self.add(Cubo,ejes)
        
        self.add(ejes)
        self.add_fixed_in_frame_mobjects(Joystick)
        self.play(Create(Joystick),Create(Cubo))
        self.wait()
        #self.move_camera(phi=60 * DEGREES, theta=-70 * DEGREES)
        #self.begin_ambient_camera_rotation(rate=-PI/20, about="theta")
          
        #self.wait(15)
        #self.stop_ambient_camera_rotation()
        
        #animaciones
        Cubo.save_state()
        CircInt.save_state()
        angulo.set_value(PI / 2)
        #mover hacia arriba
        
        self.play(magnitud.animate.increment_value(8))
        
        #mover hacia abajo
        angulo.set_value(-PI / 2)
        magnitud.set_value(0)
        
        self.play(magnitud.animate.increment_value(8))
        
        #mover en angulo 2PI/3
        angulo.set_value(2*PI/6)
        magnitud.set_value(0)
        
        self.play(magnitud.animate.set_value(8))
        
        #mover en angulo 11PI/6
        angulo.set_value(11*PI/6)
        magnitud.set_value(0)
        
        self.play(magnitud.animate.set_value(8))
        
        #mover al centro
        magnitud.set_value(0)
        self.play(Restore(Cubo),Restore(CircInt))

        self.wait()

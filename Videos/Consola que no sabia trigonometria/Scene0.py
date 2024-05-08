from manim import *

# Creamos figuras y se seccionan con plano


class Scene0(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES)
        # elf.set_camera_orientation(phi=0 * DEGREES, theta=180 * DEGREES)
        Ejes = ThreeDAxes()

        # resolucion de circulos
        resolucion = (10, 10)

        # alto de palanca
        alto = 2

        # radio de circunferencia
        radio = 0.3

        # base del joystick
        Base = Prism(dimensions=(2.5, 2.5, 0.4))

        # palanca de joystick
        Palanca = Cylinder(radius=radio, height=alto, resolution=resolucion)
        Palanca.set_fill(color=YELLOW, opacity=1)

        # rodillo de palanca
        Rodillo = Sphere(center=(0, 0, 0.4), radius=radio, resolution=resolucion)
        Rodillo.set_fill(color=YELLOW, opacity=1)

        # potencimetro x
        pX = Cylinder(radius=0.5, height=0.5, direction=X_AXIS)
        pX.set_fill(color=GREEN, opacity=1)

        # potencionmetro Y
        pY = Cylinder(radius=0.5, height=0.5, direction=Y_AXIS)
        pY.set_fill(color=GREEN, opacity=1)
        # armado de joystick
        Palanca.move_to(Base.get_center() + [0, 0, alto / 2 + 0.4])

        pX.move_to(Base.get_center() + [2.5 / 2, 0, 0])
        pY.move_to(Base.get_center() + [0, -1 * 2.5 / 2, 0])
        Joystick = VGroup()
        Joystick.add(Base, Palanca, Rodillo, pX, pY)
        # updater texto

        Vx = MathTex(r"V_x=0").to_edge(
                UP + RIGHT
            )
        Vy = MathTex(r"V_y=0").next_to(Vx,DOWN)
        
        self.add_fixed_in_frame_mobjects(Vx)
        self.add_fixed_in_frame_mobjects(Vy)
        valueX = ValueTracker(0)
        valueY = ValueTracker(0)

        def update_vx(obj):

            obj.become(MathTex(r"V_x=" + str(round(valueX.get_value(), 2)))).to_edge(
                UP + RIGHT
            )
            self.add_fixed_in_frame_mobjects(obj)

        def update_vy(obj):

            obj.become(MathTex(r"V_y=" + str(round(valueY.get_value(), 2)))).next_to(
                Vx, DOWN
            )
            self.add_fixed_in_frame_mobjects(obj)

        Vx.add_updater(update_vx)
        Vy.add_updater(update_vy)

        # animacion
        #self.add(Joystick, Ejes, Vx,Vy)
        Palanca.save_state()
        Rodillo.save_state()
        pY.save_state()
        pX.save_state()

        self.add(Ejes)
        self.play(FadeIn(Joystick))
        # self.play(
        #     Rotate(mobject=Palanca, angle=PI / 4, axis=Y_AXIS, about_point=(0, 0, 0.4)),
        #     Rotate(mobject=Rodillo, angle=PI / 4, axis=Y_AXIS),
        #     Rotate(mobject=pY, angle=PI / 4, axis=Y_AXIS),
        #     valueY.animate.set_value(1.5),
        # )

        # self.play(
        #     Rotate(
        #         mobject=Palanca, angle=-PI / 2, axis=Y_AXIS, about_point=(0, 0, 0.4)
        #     ),
        #     Rotate(mobject=Rodillo, angle=-PI / 2, axis=Y_AXIS),
        #     Rotate(mobject=pY, angle=-PI / 2, axis=Y_AXIS),
        #     valueY.animate.set_value(-1.5)
        # )

        # self.play(Restore(Palanca), Restore(Rodillo),Restore(pY),valueY.animate.set_value(0))
        

        # self.play(
        #     Rotate(
        #         mobject=Palanca,
        #         angle=PI / 4,
        #         axis=Y_AXIS + X_AXIS,
        #         about_point=(0, 0, 0.4),
        #     ),
        #     Rotate(mobject=pY, angle=PI / 4, axis=Y_AXIS),
        #     Rotate(mobject=pX, angle=PI / 4, axis=X_AXIS),
        #     valueX.animate.set_value(1.5),
        #     valueY.animate.set_value(1.5),
        # )

        # self.play(
        #     Rotate(
        #         mobject=Palanca,
        #         angle=-PI / 2,
        #         axis= Y_AXIS,
        #         about_point=(0, 0, 0.4),
        #     ),
        #     Rotate(mobject=pY, angle=-PI / 2, axis=Y_AXIS),
        #     valueY.animate.set_value(0)
        # )

        # self.play( Restore(Palanca),Restore(pY),Restore(pX),valueX.animate.set_value(0),valueY.animate.set_value(0))

        self.wait()

from manim import *
import math
import numpy

# Creamos figuras y se seccionan con plano


class Scene3_1(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=60 * DEGREES, theta=-70 * DEGREES)
        Cubo = Cube(side_length=1, fill_opacity=1, fill_color=YELLOW, stroke_width=3)
        Cubo.set_stroke(color=GRAY)
        Cubo.move_to([1, 1, 1])
        # Ejes
        Ejes = ThreeDAxes(
            x_range=[-7, 7, 1], y_range=[-7, 7, 1], x_length=12, y_length=12
        )
        self.add(Ejes)
        # punto de rotacion
        Punto = Dot3D([1, 1, 1])

        # Estela
        estelaPunto = TracedPath(
            Punto.get_center, dissipating_time=0.6, stroke_opacity=[0, 1]
        )
       

        # -------------------matrices de rotacion
        tRx = r"R_x(\theta)=\begin{bmatrix} 1 & 0 & 0\\ 0 & \cos(\theta) & -\sin(\theta) \\ 0 & \sin(\theta) & \cos(\theta) \end{bmatrix}"

        tRy = r"R_y(\theta)=\begin{bmatrix} \cos(\theta) & 0 & \sin(\theta) \\ 0 & 1 & 0 \\  -\sin(\theta) & 0 & \cos(\theta) \end{bmatrix}"

        tRz = r"R_z(\theta)=\begin{bmatrix} \cos(\theta) & -\sin(\theta) & 0 \\ \sin(\theta)   & \cos(\theta)  & 0 \\  0 & 0 & 1 \end{bmatrix}"

        Rx = MathTex(tRx, font_size=30).to_edge(UR)
        Ry = MathTex(tRy, font_size=30).next_to(Rx, DOWN, buff=0.7)
        Rz = MathTex(tRz, font_size=30).next_to(Ry, DOWN, buff=0.7)

        def update_text(obj):
            (x, y, z) = Punto.get_center()

            newP = MathTex(
                f"p=({ int(x) if x-int(x)==0 else round(x,2) },{ int(y)  if y-int(y)==0 else round(y,2)},{int(z) if z-int(z) ==0 else round(z,2)}  )",
                font_size=30,
            )
            newP.move_to(obj.get_center())

            obj.become(newP)
            self.add_fixed_in_frame_mobjects(obj)

        def update_cordenadas(obj):

            puntos_cubo = Cubo.get_all_points()
            p1 = puntos_cubo[0]
            p2 = puntos_cubo[3]
            p3 = puntos_cubo[7]
            p4 = puntos_cubo[11]
            p5 = p1 + [0, 0, 1]
            p6 = p2 + [0, 0, 1]
            p7 = p3 + [0, 0, 1]
            p8 = p6 + [0, 0, 1]
            cordenadas = [p1, p2, p3, p4, p5, p6, p7, p8]

            cord1 = MathTex(
                f"p_0=({ int(p1[0]) if p1[0]-int(p1[0])==0 else round(p1[0],2) },{ int(p1[1])  if p1[1]-int(p1[1])==0 else round(p1[1],2)},{int(p1[2]) if p1[2]-int(p1[2]) ==0 else round(p1[2],2)}  )",
                font_size=25,
            ).move_to(obj[0].get_center())

            obj[0].become(cord1)

            for i in range(1, 8):
                temp = MathTex(
                    f"p_{i}=({ int(cordenadas[i][0]) if cordenadas[i][0]-int(cordenadas[i][0])==0 else round(cordenadas[i][0],2) },{ int(cordenadas[i][1])  if cordenadas[i][1]-int(cordenadas[i][1])==0 else round(cordenadas[i][1],2)},{int(cordenadas[i][2]) if cordenadas[i][2]-int(cordenadas[i][2]) ==0 else round(cordenadas[i][2],2)}  )",
                    font_size=25,
                ).next_to(obj[i - 1], DOWN)
                obj[i].become(temp)
            self.add_fixed_in_frame_mobjects(obj)

        # ----------------Cordenadas-----------------------------------------
        # cordenadas del punto p

        pCordenadas = MathTex(r"p=(x_1,y_1,z_1)", font_size=30).next_to(Rx, DOWN)

        puntos_cubo = Cubo.get_all_points()
        p1 = puntos_cubo[0]
        p2 = puntos_cubo[3]
        p3 = puntos_cubo[7]
        p4 = puntos_cubo[11]
        p5 = p1 + [0, 0, 1]
        p6 = p2 + [0, 0, 1]
        p7 = p3 + [0, 0, 1]
        p8 = p6 + [0, 0, 1]
        cordenadas = [p1, p2, p3, p4, p5, p6, p7, p8]

        cord1 = MathTex(
            f"p_0=({ int(p1[0]) if p1[0]-int(p1[0])==0 else round(p1[0],2) },{ int(p1[1])  if p1[1]-int(p1[1])==0 else round(p1[1],2)},{int(p1[2]) if p1[2]-int(p1[2]) ==0 else round(p1[2],2)}  )",
            font_size=25,
        ).to_edge(UL)

        textoCordenadas = VGroup()
        textoCordenadas.add(cord1)

        for i in range(1, 8):
            temp = MathTex(
                f"p_{i}=({ int(cordenadas[i][0]) if cordenadas[i][0]-int(cordenadas[i][0])==0 else round(cordenadas[i][0],2) },{ int(cordenadas[i][1])  if cordenadas[i][1]-int(cordenadas[i][1])==0 else round(cordenadas[i][1],2)},{int(cordenadas[i][2]) if cordenadas[i][2]-int(cordenadas[i][2]) ==0 else round(cordenadas[i][2],2)}  )",
                font_size=25,
            ).next_to(textoCordenadas[i - 1], DOWN)
            textoCordenadas.add(temp)

        # -------------Animacion inicial------------------------------------
        # self.set_camera_orientation(phi=0, theta=3*PI/2)
        self.move_camera(phi=60 * DEGREES, theta=-70 * DEGREES)
        self.begin_ambient_camera_rotation(rate=-PI/20, about="theta")
        
        self.wait()
        self.add(estelaPunto)
        pCordenadas.add_updater(update_text)
        self.play(Create(Punto))
        self.wait()
        
        self.add_fixed_in_frame_mobjects(pCordenadas,Rx)
        self.play(FadeIn(pCordenadas),FadeIn(Rx))
        #Rotacion en eje x
        self.stop_ambient_camera_rotation()
        self.wait()
        self.play(Rotate(Punto, angle=2 * PI, axis=X_AXIS, about_point=ORIGIN))
        self.wait()
        
        ##Rotacion en eje y
        Ry.move_to(Rx.get_center())
        Ry.set_opacity(0)
        self.add_fixed_in_frame_mobjects(Ry)
        self.play(ReplacementTransform(Rx, Ry), Ry.animate.set_opacity(1))
        self.wait()
        del estelaPunto

        estelaPunto = TracedPath(
            Punto.get_center, dissipating_time=0.6, stroke_opacity=[0, 1]
        )
        self.add(estelaPunto)
        self.play(Rotate(Punto, angle=2 * PI, axis=Y_AXIS, about_point=ORIGIN))

        ##Rotacion en eje z
        Rz.move_to(Rx.get_center())
        Rz.set_opacity(0)
        self.add_fixed_in_frame_mobjects(Rz)
        self.play(ReplacementTransform(Ry, Rz), Rz.animate.set_opacity(1))
        self.wait()
        del estelaPunto

        estelaPunto = TracedPath(
            Punto.get_center, dissipating_time=0.6, stroke_opacity=[0, 1]
        )
        self.add(estelaPunto)
        self.play(Rotate(Punto, angle=2 * PI, axis=Z_AXIS, about_point=ORIGIN))
        textoCordenadas.set_opacity(0)
        self.add_fixed_in_frame_mobjects(textoCordenadas)
        pCordenadas.remove_updater(update_text)
        # -------------------------------Rotaciones con cubo
        self.wait(2)
        self.play(
            ReplacementTransform(Punto, Cubo),
            Uncreate(pCordenadas),
            textoCordenadas.animate.set_opacity(1),
        )
        
        textoCordenadas.add_updater(update_cordenadas)

        Rx.set_opacity(0)
        self.add_fixed_in_frame_mobjects(Rx)
        self.wait()
        self.play(
            Rotate(Cubo, angle=2 * PI, axis=X_AXIS, about_point=ORIGIN),
            ReplacementTransform(Rz, Rx),
            Rx.animate.set_opacity(1),
            Uncreate(pCordenadas)
        )
        Ry.move_to(Rx.get_center())
        Ry.set_opacity(0)
        self.add_fixed_in_frame_mobjects(Ry)
        self.play(ReplacementTransform(Rx, Ry), Ry.animate.set_opacity(1))
        self.play(Rotate(Cubo, angle=2 * PI, axis=Y_AXIS, about_point=ORIGIN))
        Rz.set_opacity(0)
        Rz.move_to(Ry.get_center())
        self.add_fixed_in_frame_mobjects(Rz)
        self.play(ReplacementTransform(Ry, Rz), Rz.animate.set_opacity(1))
        self.play(Rotate(Cubo, angle=2 * PI, axis=Z_AXIS, about_point=ORIGIN))

        ##Rotaciones con el mismo Eje
        # --------se muestra centro gemetrico

        # ----temporal
        self.play(FadeOut(Rz))

        centro = Dot3D(Cubo.get_center())
        flecha = Arrow3D(
            start=[2, 2, 2], end=centro.get_center() + [0.1, 0.1, 0.1], resolution=2
        )
        # --------Texto flecha
        f1 = MathTex(r"p_c=(x_c,y_c,z_c)", font_size=35).next_to(
            flecha, UP + RIGHT, buff=0.5
        )

        # self.add(flecha)
        self.add(centro)
        self.play(Cubo.animate.set_opacity(0.2))
        self.add_fixed_in_frame_mobjects(f1)
        self.play(FadeIn(flecha), FadeIn(f1))
        self.play(FadeOut(flecha), FadeOut(f1), Cubo.animate.set_opacity(1))
        self.remove(flecha, f1, centro)

        # rotaciones
        Rx.set_opacity(0)
        self.add_fixed_in_frame_mobjects(Rx)

        self.play(
            Rotate(Cubo, angle=2 * PI, axis=X_AXIS, about_point=Cubo.get_center()),

            Rx.animate.set_opacity(1),
        )
        Ry.move_to(Rx.get_center())
        Ry.set_opacity(0)
        self.add_fixed_in_frame_mobjects(Ry)
        self.play(ReplacementTransform(Rx, Ry), Ry.animate.set_opacity(1))

        self.play(
            Rotate(Cubo, angle=2 * PI, axis=Y_AXIS, about_point=Cubo.get_center())
        )
        Rz.set_opacity(0)
        Rz.move_to(Ry.get_center())
        self.add_fixed_in_frame_mobjects(Rz)
        self.play(ReplacementTransform(Ry, Rz), Rz.animate.set_opacity(1))
        self.play(
            Rotate(Cubo, angle=2 * PI, axis=Z_AXIS, about_point=Cubo.get_center())
        )
        self.wait()

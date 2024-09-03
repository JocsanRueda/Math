from manim import *
import math
import numpy

# Creamos figuras y se seccionan con plano


class Scene3(Scene):
    def RotacionX(self, punto, angulo):
        cos = np.array(
            [
                [1, 0, 0],
                [0, math.cos(angulo), -1 * math.sin(angulo)],
                [0, math.sin(angulo), math.cos(angulo)],
            ]
        )

        return np.dot(punto, cos)

    def construct(self):

        tRy = r"R_y(\theta)=\begin{bmatrix} \cos(\theta) & 0 & \sin(\theta) \\ 0 & 1 & 0 \\  -\sin(\theta) & 0 & \cos(\theta) \end{bmatrix}"

        tRz = r"R_z(\theta)=\begin{bmatrix} \cos(\theta) & -\sin(\theta) & 0 \\ \sin(\theta)   & \cos(\theta)  & 0 \\  0 & 0 & 1 \end{bmatrix}"

        Rx = MathTex(
            r"R_x(\theta)",
            r"=\begin{bmatrix} 1 & 0 & 0\\ 0 & \cos(\theta) & -\sin(\theta) \\ 0 & \sin(\theta) & \cos(\theta) \end{bmatrix}",
            font_size=45,
        )

        punto = Dot([1, 1, 1])
        pCordenadas = MathTex(r"p", r"=[x_0,y_0,z_0]", font_size=45).next_to(
            Rx, DOWN, buff=1
        )

        f1 = MathTex(
            r"p", r" \cdot", r" R_x(\theta) ", "=[x_1,y_1,z_1]", font_size=45
        ).next_to(pCordenadas, DOWN, buff=1)
        rTheta = Rx[0].copy()
        rSub = pCordenadas[0].copy()

        # ----------------Valores para pi------------
        f2 = MathTex(r"0 \leq \theta \leq 2\pi").move_to(UP)
        f3 = MathTex(r"n=10").next_to(f2, DOWN)
        f4 = MathTex(r"i=\frac{2\pi}{10}").next_to(f3, DOWN)
        f5 = MathTex(r"p", r" \cdot", r" R_x(\theta) ")
        f6 = MathTex(r"(p-I)", r" \cdot", r" R_x(\theta) ")
        f7 = MathTex(r"([x_0,y_0,x_0]-[x,y,z])", r" \cdot", r" R_x(\theta) ")
        f8 = MathTex(r"R_g=d(p,I)").next_to(f7, DOWN)
        f9 = MathTex(r"x_c=\frac{x_1+x_2+x_3+x_4}{4}").to_edge(UP)
        f10 = MathTex(r"y_c=\frac{y_1+y_2+y_3+y_4}{4}").next_to(f9, DOWN)
        f11 = MathTex(r"z_c=\frac{z_1+z_2+z_3+z_4}{4}").next_to(f10, DOWN)
        f12 = MathTex(r"p_c=(x_c,y_c,z_c)").next_to(f11, DOWN)
        f13 = MathTex(r"(p-p_c)", r" \cdot", r" R_x(\theta) ").next_to(f12, DOWN)
        # ------Animacion 1----
        self.play(Write(Rx))
        self.wait()
        self.play(Rx.animate.to_edge(UP))
        Ry = MathTex(tRy, font_size=45).next_to(Rx, DOWN, buff=0.7)
        Rz = MathTex(tRz, font_size=45).next_to(Ry, DOWN, buff=0.7)
        self.play(Write(Ry))

        self.play(Write(Rz))
        self.wait()
        self.play(Uncreate(Ry), Uncreate(Rz))
        self.play(Write(pCordenadas))
        self.wait()
        self.play(
            rTheta.animate.move_to(f1[2].get_center()),
            rSub.animate.move_to(f1[0].get_center()),
        )
        self.play(Write(f1))
        self.remove(rSub, rTheta)
        self.wait()
        self.play(Uncreate(Rx), Uncreate(pCordenadas), Uncreate(f1))

        ## ------Animacion 2-------------

        self.play(Write(f2))
        self.wait()
        self.play(Write(f3))
        self.wait()
        self.play(Write(f4))
        self.wait()
        # -----------Grupo temporal
        tempGroup = VGroup()
        tempGroup.add(f2, f3, f4)
        self.play(tempGroup.animate.to_edge(UL))

        self.wait()

        # ---------------Animacion 3 posicioneas
        angulo = 0
        posiciones = VGroup()
        (x, y, z) = self.RotacionX(punto.get_center(), angulo)
        print(self.RotacionX(punto.get_center(), angulo))
        newP = MathTex(
            f"p=({ int(x) if x-int(x)==0 else round(x,2) },{ int(y)  if y-int(y)==0 else round(y,2)},{int(z) if z-int(z) ==0 else round(z,2)}  )",
            font_size=40,
        ).to_edge(UP)
        posiciones.add(newP)

        self.play(Write(newP))
        for i in range(10):
            angulo += (2 * PI) / 10
            (x, y, z) = self.RotacionX(punto.get_center(), angulo)
            tempP = MathTex(
                f"p_{i}=({ int(x) if x-int(x)==0 else round(x,2) },{ int(y)  if y-int(y)==0 else round(y,2)},{int(z) if z-int(z) ==0 else round(z,2)}  )",
                font_size=40,
            )

            tempP.next_to(posiciones[i], DOWN)
            posiciones.add(tempP)

        self.play([Write(obj) for obj in posiciones[1:]])
        self.wait()
        self.play([Uncreate(obj) for obj in posiciones], Uncreate(tempGroup))
        self.wait()

        # ----------------------Radio de Giro y punto de rotacion---------------------
        self.play(Write(f5))
        self.wait()

        self.play(TransformMatchingTex(f5, f6))
        self.wait()
        self.play(TransformMatchingTex(f6, f7))
        self.play(Write(f8))

        self.wait()
        self.play(Uncreate(f7), Uncreate(f8))
        self.wait()
        # ---------------------Centro geometrico--------------------------------------
        self.play(Write(f9), Write(f10), Write(f11))
        self.play(Write(f12))
        self.play(Write(f13))
        self.wait()

        self.wait()


def RotacionX(punto, angulo):
    cos = np.array(
        [
            [1, 0, 0],
            [0, math.cos(angulo), -1 * math.sin(angulo)],
            [0, math.sin(angulo), math.cos(angulo)],
        ]
    )

    return np.dot(np.array(punto), cos)


punto = [1, 1, 1]
angulo = 0
for i in range(10):
    angulo += (2 * math.pi) / 10
    punto2 = RotacionX(punto, angulo)

    print(punto2)

from manim import *
import math
import numpy

# Creamos figuras y se seccionan con plano


class Scene3(Scene):

    def construct(self):
        circulo = Circle(1)
        cuadrado = Square(1)
        triangulo = Triangle()
        circuloCP = circulo.copy()
        cuadradoCP = cuadrado.copy()
        self.add(circulo)
        self.play(ReplacementTransform(circuloCP, cuadradoCP))
        self.play(Uncreate(cuadrado))
        self.play(Create(circulo))

        self.play(ReplacementTransform(circulo, triangulo))
        self.play(Create(cuadrado))
        self.wait()

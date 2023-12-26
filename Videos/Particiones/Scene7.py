from manim import *

# Creamos figuras y se seccionan con plano


# Formula iterativa para particiones
class Scene7(Scene):
    def construct(self):
        def puntos_equidistantes(punto1, punto2, n):
            """
            Encuentra n puntos equidistantes entre dos puntos tridimensionales.

            Parameters:
            punto1 (np.array): Primer punto tridimensional (x1, y1, 0).
            punto2 (np.array): Segundo punto tridimensional (x2, y2, 0).
            n (int): Número de puntos equidistantes deseados.

            Returns:
            np.array: Matriz con n puntos equidistantes.
            """
            distancia_total = np.linalg.norm(punto2[:2] - punto1[:2])
            paso = distancia_total / (n + 1)

            direccion = (punto2[:2] - punto1[:2]) / distancia_total

            puntos = []
            for i in range(1, n + 1):
                punto_intermedio = punto1[:2] + i * paso * direccion
                punto_equidistante = np.array(
                    [punto_intermedio[0], punto_intermedio[1], 0]
                )
                puntos.append(punto_equidistante)

            return np.array(puntos)

        table = MathTable(
            [[1, 2, 3, 4, 5, "..."], [1, 5, 12, 22, 35, "..."]],
            row_labels=[MathTex("m"), MathTex(r"\frac{m}{2} (3m-1)")],
            include_outer_lines=True,
            line_config={"stroke_width": 1.6, "color": TEAL},
        )

        p0 = Dot()
        t1 = Text("1", font_size=30).move_to(DOWN * 2.6)
        t1.add(p0.next_to(t1, UP))
        # primer poligono
        t2 = Text("1+4=5", font_size=30).move_to(DOWN * 2.6)
        polygon1 = RegularPolygon(5, color=BLUE).scale(0.5)
        p1_Points = polygon1.get_vertices()
        p1_Points = [Dot(p) for p in p1_Points]
        [polygon1.add(p) for p in p1_Points]
        t2.add(polygon1.next_to(t2, UP))

        # segundo poligono

        t3 = Text("1+4+7=12", font_size=30).move_to(DOWN * 2.6)
        polygon2 = RegularPolygon(5, color=BLUE).scale(1)

        p2_Points = polygon2.get_vertices()

        p2_Points = [Dot(p) for p in p2_Points]
        [
            polygon2.add(Dot(p))
            for p in puntos_equidistantes(
                p2_Points[0].get_center(), p2_Points[1].get_center(), 1
            )
        ]

        [
            polygon2.add(Dot(p))
            for p in puntos_equidistantes(
                p2_Points[3].get_center(), p2_Points[4].get_center(), 1
            )
        ]

        [
            polygon2.add(Dot(p))
            for p in puntos_equidistantes(
                p2_Points[4].get_center(), p2_Points[0].get_center(), 1
            )
        ]
        [polygon2.add(p) for p in p2_Points]
        t3.add(polygon2.next_to(t3, UP))
        polygon1Copy = (
            polygon1.copy()
            .next_to(polygon2, UP, buff=-polygon2.height)
            .shift([-0.285, 0, 0])
        )
        polygon2.add(polygon1Copy)

        # tercer poligono
        t4 = Text("1+4+7+10=22", font_size=30).move_to(DOWN * 2.6).shift(2 * RIGHT)
        polygon3 = RegularPolygon(5, color=BLUE).scale(1.5)

        p3_Points = polygon3.get_vertices()
        p3_Points = [Dot(p) for p in p3_Points]
        [polygon3.add(p) for p in p3_Points]

  
        

        [
            polygon3.add(Dot(p))
            for p in puntos_equidistantes(
                p3_Points[0].get_center(), p3_Points[1].get_center(), 2
            )
        ]

        [
            polygon3.add(Dot(p))
            for p in puntos_equidistantes(
                p3_Points[3].get_center(), p3_Points[4].get_center(), 2
            )
        ]

        [
            polygon3.add(Dot(p))
            for p in puntos_equidistantes(
                p3_Points[4].get_center(), p3_Points[0].get_center(), 2
            )
        ]
        t4.add(polygon3.next_to(t4, UP))
        polygon2Copy = (
            polygon2.copy()
            .next_to(polygon3, UP, buff=-polygon3.height)
            .shift([-0.3, 0, 0])
        )
        polygon3.add(polygon2Copy)

        # Cuarto Poligono
        t5 = Text("1+4+7+10+13=35", font_size=30).move_to(DOWN * 2.6).shift(4.7 * RIGHT)
        polygon4 = RegularPolygon(5, color=BLUE).scale(2)

        p4_Points = polygon4.get_vertices()
        p4_Points = [Dot(p) for p in p4_Points]

        [
            polygon4.add(Dot(p))
            for p in puntos_equidistantes(
                p4_Points[0].get_center(), p4_Points[1].get_center(), 3
            )
        ]

        [
            polygon4.add(Dot(p))
            for p in puntos_equidistantes(
                p4_Points[3].get_center(), p4_Points[4].get_center(), 3
            )
        ]

        [
            polygon4.add(Dot(p))
            for p in puntos_equidistantes(
                p4_Points[4].get_center(), p4_Points[0].get_center(), 3
            )
        ]
        [polygon4.add(p) for p in p4_Points]
        t5.add(polygon4.next_to(t5, UP))
        polygon3Copy = (
            polygon3.copy()
            .next_to(polygon4, UP, buff=-polygon4.height)
            .shift([-0.28, 0, 0])
        )
        polygon4.add(polygon3Copy)

        cell1 = table.get_entries((2, 2))
        cell2 = table.get_entries((2, 3))
        cell3 = table.get_entries((2, 4))
        cell4 = table.get_entries((2, 5))
        cell5 = table.get_entries((2, 6))

        self.play(table.create())

        self.play(table.animate.scale(0.6))

        self.play(table.animate.move_to(UP * 3))

        self.play(Create(t1), cell1.animate.set_color(BLUE))

        self.play(t1.animate.shift(-6.85 * RIGHT))

        self.play(
            Create(t2), cell1.animate.set_color(WHITE), cell2.animate.set_color(BLUE)
        )

        self.play(t2.animate.shift(-5.5 * RIGHT))

        self.play(
            Create(t3), cell2.animate.set_color(WHITE), cell3.animate.set_color(BLUE)
        )
        self.play(t3.animate.shift(-2.9 * RIGHT))

        self.play(
            Create(t4), cell3.animate.set_color(WHITE), cell4.animate.set_color(BLUE)
        )
        self.play(t4.animate.shift(-1.5 * RIGHT))

        self.play(
            Create(t5), cell4.animate.set_color(WHITE), cell5.animate.set_color(BLUE)
        )
        self.wait()
        self.play(
            Uncreate(t5),
            Uncreate(t4),
            Uncreate(t3),
            Uncreate(t2),
            Uncreate(t1),
            Uncreate(table)
        )

        self.wait(1)
        

from manim import *


from manim import *


class Object_Dots(VGroup):
    def __init__(self, num_dots=3, color=BLUE, radius=0.1, **kwargs):
        super().__init__(
            *[Dot(color=color).scale(100) for x in range(num_dots)], **kwargs
        )


class FerrersDiagram(VGroup):
    def __init__(self, partition, dot_color=BLUE, spacing=0.2, radius=0.1, **kwargs):
        super().__init__(**kwargs)
        self.partition = partition
        self.dot_color = dot_color
        self.spacing = spacing
        self.generate_diagram()

    def generate_diagram(self):
        for row_length in self.partition:
            dots_row = Object_Dots(num_dots=row_length, color=self.dot_color)
            self.add(dots_row)
            for i, dot in enumerate(dots_row):
                dot.move_to(
                    dots_row[i].get_center()
                    + RIGHT * (i - row_length // 2) * self.spacing
                )
            self.shift(DOWN * dots_row[i].get_height() * 1.5)
        self.arrange_submobjects(DOWN, buff=self.spacing / 3, aligned_edge=LEFT)


# Método para generar el diagrama de Ferrers desde una partición
def generate_ferrers_diagram(scene, partition, spacing=0.2):
    ferrer_diagram = FerrersDiagram(partition=partition, spacing=spacing)
    return ferrer_diagram


def partitions(n, i=1):
    if n == 0:
        return [[]]
    result = []
    while i <= n:
        for p in partitions(n - i, i):
            result.append([i] + p)
        i += 1
    return result


# Ejemplo de uso
number = 4
partitions_of_4 = partitions(number)
print(partitions_of_4)


# grupo de puntos
class Object_Dots(VGroup):
    def __init__(self, num_dots=3, color=BLUE, **kwargs):
        super().__init__(*[Dot(color=color) for _ in range(num_dots)], **kwargs)


# Escena que muestra la primera parte del video
class Scen18(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        number = 27

        partition = partitions(number)
        partition = [list(reversed(p)) for p in partition]
        diagrams = []
        diagramObject = []
        # 70
        columnas = 70
        # 0.12
        space = 0.13
        for n in range(round(len(partition)*1)):
            temp = MathTex("+").scale(0.2).set_opacity(0)
            # 0.08
            diagramObject.append(
                generate_ferrers_diagram(self, partition[n]).scale(0.055)
            )

            if n < columnas:
                # Las primeras 10 particiones se colocan en la misma fila
                if n > 0:
                    temp.next_to(diagrams[n - 1], RIGHT, buff=space)
                # 3.3
                else:
                    temp.move_to(LEFT * 6.8).shift(UP * 3.15)

            else:
                # A partir de la 11ª partición, se coloca en la siguiente fila

                row_index, col_index = divmod(n - columnas, columnas)

                if col_index == 0:
                    # Salto de línea después de 10 elementos

                    temp.next_to(
                        diagrams[n - columnas],
                        DOWN,
                        buff=space*1.7,
                    )

                else:
                    # Los siguientes 9 elementos se colocan uno al lado del otro

                    temp.next_to(diagrams[n - 1], RIGHT, buff=space)

            diagrams.append(temp)

        for n in range(len(diagrams)):
            diagrams[n].add(diagramObject[n].next_to(diagrams[n], UP))

        group = VGroup(*diagrams)
       
        #0.08
        self.camera.frame.scale(0.08).move_to(group[0])
        #self.add(group)
        self.play(Create(group),Restore(self.camera.frame),run_time=len(group)*0.005)
      
    
        self.wait()
 

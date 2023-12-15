from manim import *


class Object_Dots(VGroup):
    def __init__(self, num_dots=3, color=BLUE, **kwargs):
        super().__init__(*[Dot(color=color) for x in range(num_dots)], **kwargs)


class FerrersDiagram(VGroup):
    def __init__(self, partition, dot_color=BLUE, spacing=0.2, **kwargs):
        super().__init__(**kwargs)
        self.partition = partition
        self.dot_color = dot_color
        self.spacing = spacing
        self.generate_diagram()

    def generate_diagram(self):
        max_row_length = max(self.partition)
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
def generate_ferrers_diagram(scene, partition):
    ferrer_diagram = FerrersDiagram(partition)
    return ferrer_diagram


# Ejemplo de uso
class FerrersDiagramExample(Scene):
    def construct(self):
        number = 4
        partition = partitions(number)

        diagrams = []
        for n in range(len(partition)):
            temp = generate_ferrers_diagram(self, partition[n])
            if n < 10:
                # Las primeras 10 particiones se colocan en la misma fila
                if n > 0:
                    temp.next_to(diagrams[n - 1], RIGHT)
                else:
                    temp.to_edge(LEFT)
            else:
                # A partir de la 11ª partición, se coloca en la siguiente fila
                row_index, col_index = divmod(n - 10, 10)
                if col_index == 0:
                    # Salto de línea después de 10 elementos
                    temp.next_to(diagrams[(row_index - 1) * 10], DOWN).align_to(
                        diagrams[(row_index - 1) * 10], LEFT
                    )
                else:
                    # Los siguientes 9 elementos se colocan uno al lado del otro
                    temp.next_to(diagrams[n - 1], RIGHT)

            diagrams.append(temp)

        group = VGroup(*diagrams)
        self.play(Create(group))
        self.wait()


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

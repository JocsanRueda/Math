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
class Scen1(Scene):
    def construct(self):
        variables = (
            VGroup(MathTex("A"), MathTex("R"), MathTex("r"), MathTex("d"))
            .arrange_submobjects()
            .shift(UP)
        )

        f2 = MathTex("1+1+1+1").scale(1.3).shift([0, 1, 0])
        f2Diagram = (
            generate_ferrers_diagram(self, [1, 1, 1, 1], 0.2)
            .scale(2.1)
            .next_to(f2, DOWN, buff=0.5)
        )
        f3 = MathTex("2+1+1").scale(1.3).shift([0, 1, 0])
        f3Diagram = (
            generate_ferrers_diagram(self, [2, 1, 1], 0.2)
            .scale(2.1)
            .next_to(f3, DOWN, buff=0.5)
        )
        f4 = MathTex("2+2").scale(1.3).shift([0, 1, 0])
        f4Diagram = (
            generate_ferrers_diagram(self, [2, 2], 0.2)
            .scale(2.1)
            .next_to(f4, DOWN, buff=0.5)
        )
        f5 = MathTex("3+1").scale(1.3).shift([0, 1, 0])
        f5Diagram = (
            generate_ferrers_diagram(self, [3, 1], 0.2)
            .scale(2.1)
            .next_to(f5, DOWN, buff=0.5)
        )
        f6 = MathTex("4").scale(1.3).shift([0, 1, 0])
        f6Diagram = (
            generate_ferrers_diagram(self, [4], 0.2)
            .scale(2.1)
            .next_to(f6, DOWN, buff=0.5)
        )
        # puntos

        number = 4
        partition = partitions(number)
        partition = [list(reversed(p)) for p in partition]
        diagrams = []
        diagramObject = []
        for n in range(len(partition)):
            temp = MathTex(("+".join(map(str, partition[n])))).scale(0.7)
            diagramObject.append(generate_ferrers_diagram(self, partition[n]).scale(2))

            if n < 10:
                # Las primeras 10 particiones se colocan en la misma fila
                if n > 0:
                    temp.next_to(diagrams[n - 1], RIGHT, buff=1.5)

                else:
                    temp.to_edge(LEFT, buff=1.5)

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

        for n in range(len(diagrams)):
            diagrams[n].add(diagramObject[n].next_to(diagrams[n], UP))

        self.play(Write(f2))
        self.play(Create(f2Diagram))
        self.wait(1)

        # se eliminan objectos en escena
        self.play(Uncreate(f2), Uncreate(f2Diagram))

        self.play(Write(f3))
        self.play(Create(f3Diagram))
        self.wait(1)
        # se eliminan objectos en escena
        self.play(Uncreate(f3), Uncreate(f3Diagram))

        self.play(Write(f4))
        self.play(Create(f4Diagram))
        self.wait(1)
        # se eliminan objectos en escena
        self.play(Uncreate(f4), Uncreate(f4Diagram))
        self.play(Write(f5))
        self.play(Create(f2Diagram))
        self.wait(1)
        # se eliminan objectos en escena
        self.play(Uncreate(f5), Uncreate(f5Diagram))
        self.play(Write(f6))
        self.play(Create(f6Diagram))
        self.wait(1)
        self.play(Uncreate(f6), Uncreate(f6Diagram))
        group = VGroup(*diagrams)
        formPartition = MathTex(r"p(4)=5").to_edge(UP)
        self.play(Create(group),Write(formPartition))
        self.wait()

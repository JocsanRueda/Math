from manim import *


class Partitions(Scene):
    def construct(self):
        number = 15
        objects = []
        partition = partitions(number)
        partition = [list(reversed(p)) for p in partition]
        for n in range(len(partition[0:16])):
            temp = MathTex("15=" + ("+".join(map(str, partition[n])))).scale(0.4)

            if n == 0:
                temp.to_edge(UP)

            else:
                temp.next_to(objects[n - 1], DOWN)

          
            objects.append(temp)

        self.add(*objects)


def partitions(n, i=1):
    if n == 0:
        return [[]]
    result = []
    while i <= n:
        for p in partitions(n - i, i):
            result.append([i] + p)
        i += 1
    return result

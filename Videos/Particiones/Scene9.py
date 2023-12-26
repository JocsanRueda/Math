from manim import *


class Object_Circles(VGroup):
    def __init__(self, radius, num_circles=3, color=BLUE, **kwargs):
        super().__init__(
            *[Circle(radius=radius, color=color) for _ in range(num_circles)], **kwargs
        )


class Scene9(Scene):
    def construct(self):
        circle1 = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        circle2 = Circle(radius=0.3, color=BLUE, fill_opacity=1).next_to(circle1, LEFT)
        circle3 = Circle(radius=0.3, color=BLUE, fill_opacity=1).next_to(circle1, RIGHT)
        circles = VGroup(circle1, circle2, circle3)

        rectangle1 = Rectangle(width=3, height=1, color=TEAL).set_z_index(20)
        

        square1 = Square(1, color=TEAL,stroke_opacity=0.2)
        square2 = square1.copy().next_to(square1, RIGHT, buff=0)
        square3 = square1.copy().next_to(square1, LEFT, buff=0)
        square4 = square1.copy().set_stroke(opacity=1).next_to(square2, RIGHT, buff=1)
        square5 = square1.copy().set_stroke(opacity=1).next_to(square4, RIGHT, buff=1)

        rectangle1.next_to(square3, RIGHT, buff=-1)
        box1 = VGroup(square1, square2, square3, square4, square5,rectangle1)
        box1.to_edge(LEFT)

        self.play(Create(circles))
        self.play(circles.animate.to_corner(RIGHT + UP))
        self.play(Create(box1))
        self.wait()
        self.play(box1.animate.to_edge(UP))
        self.wait()
        box2 = box1.copy()
       

        circles2 = circles.copy()
        circles3 = circles.copy()
        circles4 = circles.copy()

        self.play(box2.animate.next_to(box1, DOWN))
        box3 = box2.copy()
        
        text1 = MathTex(r"3+0+0").next_to(box2, RIGHT, buff=4)
        self.play(
            circles2.submobjects[0].animate.move_to(box2.submobjects[0].get_center()),
            circles2.submobjects[1].animate.move_to(box2.submobjects[1].get_center()),
            circles2.submobjects[2].animate.move_to(box2.submobjects[2].get_center()),
            Write(text1),
        )
        self.play(box3.animate.next_to(box2, DOWN))
        box4 = box3.copy()
        text2 = MathTex(r"1+1+1").next_to(box3, RIGHT, buff=4)

        self.play(
            circles3.submobjects[0].animate.move_to(box3.submobjects[1].get_center()),
            circles3.submobjects[1].animate.move_to(box3.submobjects[3].get_center()),
            circles3.submobjects[2].animate.move_to(box3.submobjects[4].get_center()),
            Write(text2),
        )
        self.play(box4.animate.next_to(box3, DOWN))
        text3 = MathTex(r"2+1").next_to(box4, RIGHT, buff=4)

        self.play(
            circles4.submobjects[0].animate.move_to(box4.submobjects[0].get_center()),
            circles4.submobjects[1].animate.move_to(box4.submobjects[2].get_center()),
            circles4.submobjects[2].animate.move_to(box4.submobjects[3].get_center()),
            Write(text3),
        )

        text4 = MathTex(r"p(3)=3").to_edge(DOWN)
        self.wait()
        self.play(Write(text4))
        self.wait()
        
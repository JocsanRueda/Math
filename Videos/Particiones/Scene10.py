from manim import *


class Object_Circles(VGroup):
    def __init__(self, radius, num_circles=3, color=BLUE, **kwargs):
        super().__init__(
            *[Circle(radius=radius, color=color) for _ in range(num_circles)], **kwargs
        )


class Scene10(Scene):
    def construct(self):
        circle1 = Circle(radius=0.2, color=BLUE, fill_opacity=1)
        circle2 = Circle(radius=0.2, color=BLUE, fill_opacity=1).next_to(circle1, LEFT)
        circle3 = Circle(radius=0.2, color=BLUE, fill_opacity=1).next_to(circle1, RIGHT)
        circle4 = Circle(radius=0.2, color=BLUE, fill_opacity=1).next_to(circle3, RIGHT)
        circles = VGroup(circle1, circle2, circle3, circle4)

        rectangle1 = Rectangle(width=0.8 * 4, height=0.8, color=TEAL).set_z_index(20)
        rectangle2 = Rectangle(width=0.8 * 2, height=0.8, color=TEAL).set_z_index(20)

        square1 = Square(0.8, color=TEAL, stroke_opacity=0.2)
        square2 = square1.copy().next_to(square1, RIGHT, buff=0)
        square3 = square1.copy().next_to(square1, LEFT, buff=0)
        square4 = square1.copy().next_to(square2, RIGHT, buff=0)
        square5 = square1.copy().next_to(square4, RIGHT, buff=0.5)
        square6 = square1.copy().next_to(square5, RIGHT, buff=0)
        square7 = square1.copy().set_stroke(opacity=1).next_to(square6, RIGHT, buff=0.5)
        square8 = square1.copy().set_stroke(opacity=1).next_to(square7, RIGHT, buff=0.5)

        rectangle1.next_to(square3, RIGHT, buff=-0.8)
        rectangle2.next_to(square5, RIGHT, buff=-0.8)
        box1 = VGroup(
            square1,
            square2,
            square3,
            square4,
            square5,
            square6,
            square7,
            square8,
            rectangle1,
            rectangle2,
        )

        box1.move_to(LEFT * 1.6)

        self.play(Create(circles))
        self.play(circles.animate.to_corner(RIGHT + UP))
        self.play(Create(box1))
        self.wait()
        self.play(box1.animate.to_edge(UP))

        box2 = box1.copy()

        circles2 = circles.copy()
        circles3 = circles.copy()
        circles4 = circles.copy()
        circles5 = circles.copy()
        circles6 = circles.copy()

        self.play(box2.animate.next_to(box1, DOWN))
        box3 = box2.copy()

        text1 = MathTex(r"4+0+0+0").next_to(circles, DOWN, buff=0.8).scale(0.8)
        self.play(
            circles2.submobjects[0].animate.move_to(box2.submobjects[0].get_center()),
            circles2.submobjects[1].animate.move_to(box2.submobjects[1].get_center()),
            circles2.submobjects[2].animate.move_to(box2.submobjects[2].get_center()),
            circles2.submobjects[3].animate.move_to(box2.submobjects[3].get_center()),
            Write(text1),
        )

        self.play(box3.animate.next_to(box2, DOWN))
        box4 = box3.copy()
        text2 = MathTex(r"3+1").next_to(text1, DOWN, buff=0.8).scale(0.8)
        self.play(
            circles3.submobjects[0].animate.move_to(box3.submobjects[0].get_center()),
            circles3.submobjects[1].animate.move_to(box3.submobjects[1].get_center()),
            circles3.submobjects[2].animate.move_to(box3.submobjects[2].get_center()),
            circles3.submobjects[3].animate.move_to(box3.submobjects[4].get_center()),
            Write(text2),
        )

        self.play(box4.animate.next_to(box3, DOWN))
        box5 = box4.copy()
        text3 = MathTex(r"2+2").next_to(text2, DOWN, buff=0.8).scale(0.8)
        self.play(
            circles4.submobjects[0].animate.move_to(box4.submobjects[2].get_center()),
            circles4.submobjects[1].animate.move_to(box4.submobjects[0].get_center()),
            circles4.submobjects[2].animate.move_to(box4.submobjects[4].get_center()),
            circles4.submobjects[3].animate.move_to(box4.submobjects[5].get_center()),
            Write(text3),
        )
        self.play(box5.animate.next_to(box4, DOWN))
        box6 = box5.copy()
        text4 = MathTex(r"2+1+1").next_to(text3, DOWN, buff=0.8).scale(0.8)
        self.play(
            circles5.submobjects[0].animate.move_to(box5.submobjects[2].get_center()),
            circles5.submobjects[1].animate.move_to(box5.submobjects[0].get_center()),
            circles5.submobjects[2].animate.move_to(box5.submobjects[4].get_center()),
            circles5.submobjects[3].animate.move_to(box5.submobjects[6].get_center()),
            Write(text4),
        )

        self.play(box6.animate.next_to(box5, DOWN))

        text5 = MathTex(r"1+1+1+1").next_to(text4, DOWN, buff=0.8).scale(0.8)
        self.play(
            circles6.submobjects[0].animate.move_to(box6.submobjects[2].get_center()),
            circles6.submobjects[1].animate.move_to(box6.submobjects[7].get_center()),
            circles6.submobjects[2].animate.move_to(box6.submobjects[4].get_center()),
            circles6.submobjects[3].animate.move_to(box6.submobjects[6].get_center()),
            Write(text5),
        )

        text6 = MathTex(r"p(4)=5").to_edge(DOWN)
        self.wait()
        self.play(Write(text6))

        self.wait()

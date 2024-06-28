from manim import *
import math
import numpy

# Creamos figuras y se seccionan con plano


class Scene3(ZoomedScene):
    
    
    # contributed by TheoremofBeethoven, www.youtube.com/c/TheoremofBeethoven
    def __init__(self, **kwargs):
        width_frame = 1
        ZoomedScene.__init__(
            self,
            zoom_factor=1,
            zoomed_display_height=width_frame,
            zoomed_display_width=width_frame,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 2,
            },
            **kwargs,
        )

    def getRepisa(self, l, num, color):
        repisa = VGroup()
        index_repisa = VGroup()
        values=VGroup()
        for i in range(num):
            floor = Square(side_length=l, color=color)
            repisa.add(floor)

            if i > 0:
                floor.next_to(repisa[i - 1], DOWN, buff=0)
            text = MathTex(str(i)).move_to(floor.get_center())
            value = MathTex(str(round(math.sin(i * (PI / 180)),4) )).move_to(floor.get_center()).scale(0.6)
            values.add(value)
            index_repisa.add(text)

        return VGroup(repisa, index_repisa,values).move_to(ORIGIN)

    def construct(self):
        f1 = MathTex(r"3.5^\circ")
        f2 = MathTex(r"4^\circ")
        f3 = MathTex(r"4")

        arreglo = self.getRepisa(1, 6, BLUE)
      
        f4 = (
            MathTex(r"\sin( \theta )", r" \hspace{0.2cm},  ", r"\theta=0,1,2,3,4,5")
            .scale(0.8)
            .next_to(arreglo, UP)
        )

        # modificamos el texto
        self.play(Write(f1))
        self.wait()
        self.play(ReplacementTransform(f1, f2))
        self.wait()
        self.play(f2.animate.to_edge(LEFT))

        # mostramos la repisa
        self.play(Create(arreglo[0]))
        self.wait()
        self.play(Write(arreglo[1]), Write(f4))
        self.play(arreglo[1].animate.next_to(arreglo[0], LEFT))
        self.wait()
        self.play(Write(arreglo[2]))

        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display

        frame = zoomed_camera.frame

        zoomed_display_frame = zoomed_display.display_frame

        frame.align_to(arreglo[0][0], UP + RIGHT)
        origen = frame.get_center()

        frame.set_color(YELLOW)
        zoomed_display_frame.set_color(BLUE)
        zoomed_display.shift(DOWN).shift([-2,0,0])

        zd_rect = BackgroundRectangle(
            zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF
        )
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(
            zd_rect, lambda rect: rect.replace(zoomed_display)
        )

        self.play(Create(frame))
        self.activate_zooming()
        
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        self.play(ScaleInPlace(zoomed_display,1.5))
        
        self.play(frame.animate.shift([0,-4,0]))
        
        self.wait()
        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            rate_func=lambda t: smooth(1 - t),
        )
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        
     
        self.wait()


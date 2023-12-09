
from manim import *
class Escena4(Scene):
  def construct(self):
    c1=Circle(radius=1,color=RED)
    c2=Circle(radius=1,color=BLUE)
    c3=Circle(radius=1,color=GREEN)
    c1.move_to((-3,0,0))
    c3.move_to((3,0,0))
    cs1=c1.copy()
    cs1.set_color(WHITE)
    cs2=c2.copy()
    cs2.set_color(WHITE)
    
    pc1=Dot(c1.get_center())
    r1=Dot(c1.point_at_angle(PI))
    pc2=Dot(c2.get_center())
    r2=Dot(c2.point_at_angle(PI))

    
    texto=Text("d=0",font_size=20).to_edge(UP)
    area1=MathTex("A_1",font_size=30)
    area2=MathTex("A_2",font_size=30)
    area3=MathTex(r"\pi cm^2 \approx 3.142cm^2",font_size=30)
    R=MathTex("R=1")
    R.to_corner(LEFT+UP)
    r=MathTex(r" r",font_size=30)
    dr=MathTex(r" d",font_size=30)
    
    area3.next_to(c3,UP)
    simbolo=MathTex(" + ",font_size=30)
    simbolo2=MathTex(" = ",font_size=30)
  
    area1.next_to(cs1,UP)
    simbolo.next_to(area1,RIGHT,buff=1.5)
    simbolo2.next_to(area3,LEFT,buff=0.8)
    ap1=area1.get_center()
    area2.next_to(cs2,UP)
    ap2=area2.get_center()

    slider=Dot((0,0,0)).set_opacity(0)

    radio1=Line(r1,pc1)
    radio2=Line(r2,pc2)
    r.next_to(radio1,UP)
    dr.next_to(radio2,UP)
    ejes=Axes()
    self.add(
    
        c1,
        c2,
        c3,
        texto,
        pc1,
        pc2,
        r1,
        r2,
        radio1,
        radio2
    )

    def d_updater(obj):
      obj.become(Text("d="+str(round(slider.get_x(),2)),font_size=20).to_edge(UP))
    def area1_updater(obj):
      obj.become(MathTex(str(round((1-slider.get_x()**2)*PI,3))+"cm^2",font_size=30).move_to(ap1))
    def area2_updater(obj):
      obj.become(MathTex(str(round(((slider.get_x()**2))*PI,3))+"cm^2",font_size=30).move_to(ap2)) 

    def r2_updater(obj):
      obj.move_to(cs2.point_at_angle(PI))

    def r1_updater(obj):
      obj.move_to(cs1.point_at_angle(PI))

    def radio1_updater(obj): 
      obj.put_start_and_end_on(r1.get_center(),pc1.get_center())

    def radio2_updater(obj):
      obj.put_start_and_end_on(r2.get_center(),pc2.get_center())
    def r_updater(obj):
      obj.next_to(radio1,UP)
    def dr_updater(obj):
      obj.next_to(radio2,UP)  

    r2.add_updater(r2_updater)

    r1.add_updater(r1_updater)
    
   
    self.play(
      Write(r),
      Write(dr)
    ) 
    radio2.add_updater(radio2_updater)
    radio1.add_updater(radio1_updater)
    texto.add_updater(d_updater)
    r.add_updater(r_updater)
    dr.add_updater(dr_updater)    

    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
   
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1),
        run_time=2 
       )
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
   
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1), 
        run_time=2 
       )
    
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
   
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1), 
        run_time=2 
       )
    
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
   
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1), 
        run_time=2 
       )
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
   
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1), 
        run_time=2 
       )
  
   
    area1.add_updater(area1_updater)
    area2.add_updater(area2_updater)

    radio1.remove_updater(radio1_updater)
    radio2.remove_updater(radio2_updater)
    r2.remove_updater(r2_updater)

    r1.remove_updater(r1_updater)
    r.remove_updater(r_updater)
    dr.remove_updater(dr_updater)    


    self.remove(radio1,radio2)
    
    self.play(
        Uncreate(c1),
        Uncreate(c2),
        FadeOut(dr),
        FadeOut(r),
        cs1.animate.set_fill(opacity=1,color=RED),
        cs2.animate.set_fill(opacity=1,color=BLUE),
        c3.animate.set_fill(opacity=1,color=GREEN),
        Write(area1),
        Write(area2),
        Write(area3),
        Write(simbolo),
        Write(simbolo2),
        Write(R),
        Uncreate(r1),
        Uncreate(r2),
        run_time=0.6
    )
    
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1),
        run_time=2 
       )
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1),
        run_time=2 
       )
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1),
        run_time=2 
       )  
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1),
        run_time=2 
       )
    cs2.scale(100)
    self.play(
        GrowFromCenter(cs2),
        cs1.animate.scale(0.01),
        slider.animate.move_to((1,0,0)),
        run_time=2
        )
   
    cs1.scale(100)
    self.play(
        slider.animate.move_to((0,0,0)),
        cs2.animate.scale(0.01),
        GrowFromCenter(cs1),
        run_time=2 
       )
       
   
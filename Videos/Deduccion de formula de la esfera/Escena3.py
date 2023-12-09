from manim import *
#Creamos figuras y se seccionan con plano
class Escena3(Scene):
  def construct(self):
    variables = VGroup(MathTex("A"),MathTex("R"), MathTex("r"), MathTex("d")).arrange_submobjects().shift(UP)
    Circulo=Circle(radius=2,color=BLUE)
    Circulo.set_fill(color=BLUE)
    
    pc=Dot(Circulo.get_center())
    
    pe=Dot(pc.get_center())
    pe=Dot(Circulo.point_at_angle(0))
    radio=Line(pc,pe)
    r=MathTex("r")
    r.next_to(radio,UP)

    f1=MathTex("Area=\pi r ^2").scale(1.2)
    f2=MathTex("{{A}}","=","\pi", "{{R}}^2").scale(1.2)
    f3=MathTex("{{R}}^2","=","{{d}}^2","+","{{r}}^2").scale(1.2)
    f4=MathTex("\pi", "{{R}}^2","=","\pi", "(","{{d}}^2","+","{{r}}^2",")").scale(1.2)
    f5=MathTex("\pi", "{{R}}^2","=","\pi", "{{d}}^2","+", "\pi", "{{r}}^2").scale(1.2)
    f1.to_corner(UP)
    f2.next_to(f1,DOWN)
    f3.next_to(f2,RIGHT,buff=1)
    f4.next_to(f2,DOWN)
    f5.next_to(f4,DOWN)
    sb1=SurroundingRectangle(f5[4:7],color=BLUE)
    sb2=SurroundingRectangle(f5[8:],color=RED)
    sb3=SurroundingRectangle(f5[0:3],color=GREEN)
    t1=MathTex("A_{se}",color=RED)
    t2=MathTex("A_{co}",color=BLUE)
    t3=MathTex("A_{ci}",color=GREEN)
    t1.next_to(sb2,DOWN)

    t2.next_to(sb1,DOWN)
    t3.next_to(sb3,DOWN)


    self.play(
      Create(Circulo))
    self.wait(6)
    self.play(
      Create(pc),
      Create(pe)
      )
    
   
    def line_updater(obj):
      obj.put_start_and_end_on(pc.get_center(),pe.get_center())
    def r_updater(obj):
      obj.next_to(radio,UP)

    radio.add_updater(line_updater)
    r.add_updater(r_updater)

    self.play(
      Create(radio),
      Write(r)
    )
    self.play(
      MoveAlongPath(pe,Circulo),
      run_time=1.5
    )
    self.wait(4)
    radio.remove_updater(line_updater)
    r.remove_updater(r_updater)

    
    t=2.4
    self.play(
      Circulo.animate.set_fill(opacity=1),
      Write(f1)
      
    )
    self.play(Write(f2 ))
    self.wait(5)
    self.play(

      Uncreate(Circulo),
      Uncreate(pe),
      Uncreate(pc),
      Uncreate(radio),
      Uncreate(r)
    )
 

    self.play(Write(f3))
    self.wait(10)
    self.play(TransformMatchingTex(Group(f3,variables),f4),run_time=t/1.9)
    self.wait(t)
    self.play(TransformMatchingTex(f4,f5),run_time=t/1.9)
    self.wait(t)
    self.play(
      Create(sb1),
      Create(sb2),
      Create  (sb3),
      Write(t1),
      Write(t2),
      Write(t3)
    )
    self.wait(5)
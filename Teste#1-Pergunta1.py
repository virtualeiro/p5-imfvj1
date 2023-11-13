from p5 import *
def setup():
    size (400,300)

def draw():
     #translate(500,-200)
     background(0)
     no_stroke()
     fill(100)
     rect(145,200,10,50)
     fill(255)

     ellipse_mode(CENTER)
     ellipse(150,150,200,200)
     fill(0,0,255)
     circle(150,150,160)

     fill(255,255,255)
     begin_shape()
     vertex(100,150)
     vertex(170,130)
     vertex(170,145)
     vertex(200,145)
     vertex(200,155)
     vertex(170,155)
     vertex(170,170)
     end_shape(CLOSE)
run()

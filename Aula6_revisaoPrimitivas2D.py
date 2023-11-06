from p5 import *
from PIL import ImageGrab


def setup():
        # Sets the screen to be 720 pixels wide and 400 pixels high
        size(720, 400)
        no_loop()

def draw():
        background(0)
        
        stroke_cap(PROJECT)
        stroke_weight(30)
        stroke(233,10,10)
        line((10,10), (100,10))

        fill(102)
        no_stroke()
        rect_mode(CORNER)
        rect((81, 81), 63, 63)

        fill(255)
        ellipse((252, 144), 72, 72)

        fill(255)
        arc((479, 300), 280, 280, PI, TWO_PI)

        fill(200,0,0)
        circle((400, 100), 150)

        stroke_weight(20)
        point(500,10)
        point(500,40)
        point(500,70)
    
        fill(0,255,0) 
        quad((510,101), (520,201), (550,101), (530,125))

        no_stroke()
        fill(204)
        
        square((200,300), 100)
        fill(204)
        triangle((18, 18), (18, 360), (81, 360))

        fill(255,255,0)
        stroke(233)
        stroke_cap(ROUND)
        stroke_weight(10)
        begin_shape()
        vertex(10,300)
        vertex(200,200)
        vertex(100,100)
        vertex(10,300)
        end_shape(CLOSE)


if __name__ == '__main__':
        run()
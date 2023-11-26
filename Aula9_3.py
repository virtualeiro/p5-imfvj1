from p5 import *

def setup():
    size(400, 400)
    background(255)
    stroke(0)
    no_fill()

def draw():    
    # Parameters for the serpentine curve
    a = 100
    b = 200
    
    begin_shape()
    for t in range(1,360):
        t = radians(t)
        #x = a * atan(t)
        x = a * 1/tan(t)
        y = b * sin(t)* cos(t)
        x += width / 2
        y += height / 2
        vertex(x, y)
    end_shape()

if __name__ == '__main__':
    run()

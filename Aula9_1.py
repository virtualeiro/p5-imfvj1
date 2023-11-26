from p5 import *
x1=200
y1=200
x2=300
y2=300
def setup():
    size(400, 400)
    background(255)
    stroke(0)
    stroke_weight(2)
    
def draw():
    background(255)

    for t in range(0, 101):  # Vary t from 0 to 100
        t /= 100.0  # Normalize t to range from 0 to 1
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        point(x, y)

run()
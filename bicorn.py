from p5 import *
def bicorn():
    num_points = 1000
    a = 1
    b = 1

    beginShape()
    for t in range(num_points):
        theta = -PI + 2 * PI * t / num_points
        x = cos(theta)
        y = a * sin(theta) - b * sin(2 * theta)
        x *= 1.5  # Scale the x-coordinate to stretch the curve
        vertex(x, y)
    endShape()

def setup():
    size(400, 400)
    background(255)
    stroke(0)
    noFill()
    



def draw():
    translate(400 / 2, 400 / 2)
    scale(100)
   
    bicorn()

run()
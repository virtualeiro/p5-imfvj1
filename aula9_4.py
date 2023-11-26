from p5 import *
#Cubic Curves:
#You can create smooth curves using cubic parametric equations. 

# Define control points as lists
p0 = [50, 300]
p1 = [600, 100]
p2 = [200, 100]
p3 = [250, 300]

# Draw control points
def setup():
    size(400, 400)

    stroke(0)
    no_fill()
    stroke_weight(8)


# Draw cubic Bezier curve
def draw():
    stroke_weight(2)
    background(255)
    for t in range(101):
        t /= 100.0
        x = p0[0] * (1 - t) ** 3 + p1[0] * 3 * (1 - t) ** 2 * t + p2[0] * 3 * (1 - t) * t ** 2 + p3[0] * t ** 3
        y = p0[1] * (1 - t) ** 3 + p1[1] * 3 * (1 - t) ** 2 * t + p2[1] * 3 * (1 - t) * t ** 2 + p3[1] * t ** 3
        point(x, y)

if __name__ == '__main__':
    run()
from p5 import *
WIDTH=800
HEIGHT=600
def setup():
    size(WIDTH,HEIGHT)

def draw_rotating_rectangle(x, y, rect_size, ang):
  push_matrix()
  translate(x, y)
  rotate(ang)
  rect(0, 0, rect_size, rect_size)
  pop_matrix()

def draw():
    background(100, 200, 50)
    draw_rotating_rectangle(700, 40, 50, 5)
    draw_rotating_rectangle(10, 40, 50, 50)
    draw_rotating_rectangle(200, 40, 50, 90)

run()
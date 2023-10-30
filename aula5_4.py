from p5 import *
WIDTH=800
HEIGHT=600
def setup():
    size(WIDTH,HEIGHT)
def draw_rotating_rectangle(x, y, rect_size, ang):
  translate(x, y)
  rotate(ang)
  scale(2)
  #rect(0, 0, rect_size, rect_size)
  rect(-rect_size/2, -rect_size/2, rect_size, rect_size)
  #3 rect(50, 50, rect_size, rect_size)
  reset_matrix()

def draw():
    background(100, 200, 50)
    draw_rotating_rectangle(400, 300, 50, 45)
    draw_rotating_rectangle(400, 300, 50, 40)
    draw_rotating_rectangle(400, 300, 50, 35)
    draw_rotating_rectangle(400, 300, 50, 30)
    draw_rotating_rectangle(400, 300, 50, 25)
run()
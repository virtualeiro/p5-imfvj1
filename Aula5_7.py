from p5 import *

def setup():
  size(400, 400)

def draw():
  background(80)
  box(2,500,2)#width, height, depth, detail_x=1, detail_y=1)
  box(500,2,2)

  rotate_y(45)
  box(100,100,100)

run(mode=P3D)

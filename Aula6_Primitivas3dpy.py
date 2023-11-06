from p5 import *
def setup(): 
  size(400, 400)

def draw(): 
  background(200)

  push()
  rotateY(frame_count * 0.01)
  plane(70,100)
  pop()

  push()
  translate(-100,-100,0)
  box(70, 70, 70)
  pop()

  push()
  translate(240, -100, 0)
  rotate_z(45)
  cylinder(70, 70)
  pop()

  push()
  translate(-300, -300, 0)
  rotate_z(45)
  rotate_x(25)
  cone(50, 170)
  pop()

  push()
  translate(-75, 100, 0)  
  rotate_x(45)
  torus(50, 20)
  pop()

  push()
  translate(100, 100, 0)
  sphere(50)
  pop()

  push()
  translate(275, 100, 0)
  rotate_x(45)
  ellipsoid(30, 200, 40)

run(mode=P3D)
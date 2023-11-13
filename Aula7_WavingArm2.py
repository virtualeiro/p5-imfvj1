from p5 import *

arm_length = 100
angle = 0
angle_speed = 0.05
direction = 1

def setup():
    size(800, 600)

def draw():
    global angle, direction

    background(240)
    translate(0,100)
    sphere(100)
    translate(0,100)
    sphere(75)
    reset_matrix()

    translate(50,-50,0)
    sphere(25)
    translate(0,50,0)
    sphere(25)
    reset_matrix()

    translate(-50,-50,0)
    sphere(25)
    translate(0,50,0)
    sphere(25)
    reset_matrix()

    translate(-70,150)
    sphere(25)
    translate(-50, 0)
    sphere(25)
    translate(0, -50)
    sphere(25)
    reset_matrix()
#braço
    translate(70,150)
    sphere(25)
    translate(50, 0)
    sphere(25)
    
    angle += angle_speed * direction
    if angle > PI / 8 or angle < -PI / 8:
        direction *= -1
    rotate_z(angle)        

    sphere(25)
    translate(0, 50)
    sphere(25)
    translate(0, 50)
    sphere(25)
    translate(0, 50)
    reset_matrix()
 
run(mode="P3D")

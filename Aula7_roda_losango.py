from p5 import *
ang=0
def setup(): 
  size(800,800)

def draw():

    global ang
    box(2,500,2)
    box(500,2,2)
    background(255)

    dim=75
    ang=ang+0.01
    rotate_y(ang)
    #translate(0,200,0)
    with push_matrix():
        fill(255,0,0)
        rotate_z(math.pi/4)
        translate(dim/2,0,0)
        box(5,dim,5)
    
    with push_matrix():
        fill(0,255,0)
        rotate_z(-math.pi/4)
        translate(dim/2,0,0)
        box(5,dim,5)
       
    with push_matrix():
        fill(0,0,255)
        rotate_z(-math.pi/4)
        translate(-dim/2,0,0)
        box(5,dim,5)

    with push_matrix():
        fill(0,255,255)
        rotate_z(math.pi/4)
        translate(-dim/2,0,0)
        box(5,dim,5)

run(mode="P3D")

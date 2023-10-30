from p5 import *
WIDTH=800
HEIGHT=600
def setup():
    size(WIDTH,HEIGHT)
def draw():
    background(255)

    stroke(0,255,0)
    push_matrix()
    translate(WIDTH/2,HEIGHT/2)
    scale(2) 
    no_fill()
    quad((-20,-20), (20,-20), (20,20), (-20,20))
    pop_matrix()    
    """
    with push_matrix():
        translate(WIDTH/2,HEIGHT/2)
        scale(0.5) 
        no_fill()
        quad((-20,-20), (20,-20), (20,20), (-20,20))
    """
run()
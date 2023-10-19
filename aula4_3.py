from p5 import *
WIDTH=800
HEIGHT=600
def setup():
    size(WIDTH,HEIGHT)
def draw():
    no_fill()
    background(255)

    #1
    """
    stroke(255,0,0)
    rect(20, 20, 40, 40)
    """
    #1 e 2
    """
    stroke(0,0,255)
    scale(2.0) 
    rect(20, 20, 40, 40)
    """
    #3
    """
    stroke(255,0,0)
    rect(WIDTH/2-20, HEIGHT/2-20, 40, 40)
    """
    #3 e 4
    """
    stroke(0,255,0)
    with push_matrix():
        translate(WIDTH/2,HEIGHT/2)
        scale(2.0) 
        rect(-20, -20, 40, 40)
    """
run()
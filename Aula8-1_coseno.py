from p5 import *

x=0
y=0
ang=0
horizon=300
def setup(): 
    size(800,600)

def draw():
    background(0)
    global x,y, ang
    
    y=horizon
    ang=ang+math.pi/10
    y=y+math.cos(ang)
    circle(x,y,20)
    
    #incremento na horizontal
    x=x+1
run()
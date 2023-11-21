from p5 import *

x=0
y1=0
y2=0
ang=0
horizon=300
def setup(): 
    size(800,600)

def draw():
    background(0)
    global x,y1,y2,y3, ang
    
    #bola branca
    fill(255)
    y1=horizon
    ang=ang+math.pi/10
    y1=y1+math.cos(ang)
    circle(x,y1,20)
    
    #bola vermelha
    #amplitude 
    fill(255,0,0)
    y2=horizon/4
    y2=y2+10*math.cos(ang)
    circle(x,y2,20)
    
    #incremento na horizontal
    x=x+1

run()
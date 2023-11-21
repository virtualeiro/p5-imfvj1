from p5 import *

x=0
y1=0
y2=0
y3=0
ang=0
horizon=300
def setup(): 
    size(800,600)

def draw():
    background(0)
    global x,y1,y2,y3,y4, ang
    
    #bola branca
    #comportamento coseno
    fill(255)
    y1=horizon
    ang=ang+math.pi/10
    y1=y1+math.cos(ang)
    circle(x,y1,20)
    
    #bola vermelha
    #amplitude 
    fill(255,0,0)
    y2=horizon/2
    y2=y2+10*math.cos(ang)
    circle(x,y2,20)
    
    #bola verde
    #shift da fase
    fill(0,255,0)
    y3=3*horizon/4
    y3=y3+10*math.cos(ang+10)
    circle(x,y3,20)

    x=x+1
run()
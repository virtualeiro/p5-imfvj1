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
    global x,y1,y2,y3,y4,y5, ang
    
    #grafico coseno
    fill(255)
    y1=horizon
    ang=ang+math.pi/10
    y1=y1+math.cos(ang)
    circle(x,y1,20)
    
    #amplitude
    fill(255,0,0)
    y2=horizon/2
    y2=y2+10*math.cos(ang)
    circle(x,y2,20)
    
    #fase
    fill(0,255,0)
    y3=3*horizon/4
    y3=y3+10*math.cos(ang+10)
    circle(x,y3,20)

    #frequencia dobro
    fill(0,0,255)
    y4=6*horizon/4
    y4=y4+10*math.cos(ang*2)
    circle(x,y4,20)

    #frequencia a um quarto
    fill(0,0,255) 
    y5=7*horizon/4
    y5=y5+10*math.cos(ang*0.25)
    circle(x,y5,20)

    x=x+1
run()
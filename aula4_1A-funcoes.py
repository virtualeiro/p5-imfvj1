from p5 import *
width=800
height=600

def cruz(centroX, centroY, r, g, b):    
    fill(0)
    circle(centroX,centroY, 10)
    #stroke(255,0,0)
    stroke(r,g,b)
    comprimento=50
    metade_comprimento=comprimento/2
    line((centroX, centroY-metade_comprimento),
         (centroX, centroY+metade_comprimento) )
    line((centroX-metade_comprimento, centroY),
         (centroX+metade_comprimento, centroY) )

def myEllipse(centroX, centroY, largura, altura, r,g,b, alpha):
    fill(r,g,b, alpha)
    ellipse(centroX, centroY, largura, altura)

def setup():
    size(width,height)
def draw():
    background(255)
    #cruz(width/2, height/2, 255, 0, 0)
    #cruz(10, 50, 0, 255, 0)
    #cruz(100, 300, 0, 0, 255)
    myEllipse(width/2,height/2, 200,200, 255,0,0, 255)  
    myEllipse(280,200,300,100,0,255,0, 125)  

run()
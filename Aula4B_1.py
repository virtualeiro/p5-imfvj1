from p5 import *
height=600
width=800

def cruz(centroX, centroY):
#Faz linha vertical de comprimento 50 centrada no ponto central 
    comprimento=50
    metadeDoComprimento=25
    #centro 
    circle(centroX,centroY,10)

    stroke(255,0,0)
    line((centroX, centroY - metadeDoComprimento),(centroX, centroY + metadeDoComprimento))
    line((centroX - metadeDoComprimento, centroY),(centroX + metadeDoComprimento, centroY))

def myEllipseSimples():
    fill(255,0,0)
    ellipse(10,400, 100, 50) 

def myEllipseEficiente(x,y, largura, altura, r, g, b, alpha):
    fill(r,g,b,alpha)
    ellipse(x, y, largura, altura) 

def setup():
    size(width,height)
def draw():
    background(255)
    fill(0)
    cruz(width/2, height/2)
    cruz(20, 10)
    cruz(300, 400)

    myEllipseSimples()

    myEllipseEficiente(10,50,200,100, 126,120,10, 125)
    myEllipseEficiente(380,500,250,400, 250,0,0,170)
    myEllipseEficiente(450,250,120,19, 0,255,0,50)
    myEllipseEficiente(510,450,120,120, 0,0, 255,125)
run()
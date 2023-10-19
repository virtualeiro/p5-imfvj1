from p5 import *
import random

def setup():
    size(800,600)
    
def myellipse(x, y, width, height,r,g,b, alpha):
    stroke(r,g,b,alpha)
    fill(r,g,b,alpha)
    ellipse(x,y, width, height)

def draw():
    myellipse(200,100,300,300,255,0,0, 200)
    myellipse(100,200,300,200,125, 200, 20, 125)
    myellipse(400,300,400,250, 255, 125,0, 85)
    myellipse(300,400,500,320, 100,100,200, 15)
run()

from p5 import *
import random
#the lines begin on the top border and end on the bottom border
#the lines must be vertical.
MAXX=800
MAXY=600
def setup(): 
  size(MAXX,MAXY)
  

def draw():

  background(0)
  x1=random.randrange(0,MAXX)
  y1=random.randrange(0,MAXY)
  circle(x1, y1, 50)
  
  

run()

from p5 import *
import random
#the lines begin on the top border and end on the bottom border
#the lines must be vertical.
MAXX=800
MAXY=600
def setup(): 
  size(MAXX,MAXY)
  

def draw():


  
  stroke(random.randrange(256),random.randrange(256),random.randrange(256))
  
  distance_left = random.randrange(MAXX)
  
  line(distance_left,0, distance_left,MAXY)

run()

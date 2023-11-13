from p5 import *
import random
def setup():
  size(800,600)   
  background(0)

def draw(): 
  stroke(0, random.randrange(255), 0); 

 
  line(400, 300, random.randrange(800), random.randrange(600) )
run()
#run(mode=P3D)
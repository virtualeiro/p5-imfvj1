from p5 import *
x=0
y=0
ang=0

def setup(): 
   size(800,600)

def draw():
   global x,y,ang
   background(0)
   x=x+1
   
   ang=ang+math.pi*0.1
   #1
   y=math.sin(ang)
   #2
   y=10*math.sin(ang)
   #3
   y=100*math.sin(ang)

   translate(x,y,0) 
   box (50,50,50)
   reset_matrix()
run(mode="P3D")
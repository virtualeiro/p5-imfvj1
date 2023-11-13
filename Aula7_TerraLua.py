from p5 import *
ang=0
def setup():
     size(1000, 800) 
     
   
def draw():
#3gira a lua
     global ang
#6roda tudo     
     rotate_z(ang)

     background(0)
     fill(0,0,225)
#4tira a terra do 0
     translate(200,200,0)
#5roda a terra     
     rotate_z(ang*0.1)
     sphere(100)
     
#3gira a lua
     ang=ang+0.1
     rotate_z(ang)
#2 lua
     fill(255,0,225)       
     translate(300,0,0)
     sphere(50)
     #reset_matrix()
run(mode=P3D)
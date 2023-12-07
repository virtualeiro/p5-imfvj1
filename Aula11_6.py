from p5 import *
def setup():
     size(640, 360)
i=0
def draw():
     global i
     no_fill() 
     i=i+0.01
     
     stroke(255,255,255,50) 
     
     push_matrix()
     rotate_z(i)
     begin_shape() 
     vertex(-300, 300, -300) 
     vertex(-300, -300, -300) 
     vertex( 0, 0, 0) 
     end_shape(CLOSE)
     pop_matrix()
     
     push_matrix()
     rotate_z(-1*i)
     stroke(0,0,0,50) 
     begin_shape() 
     vertex(-300, 300, -300) 
     vertex(-300, -300, -300) 
     vertex( 0, 0, 0) 
     end_shape(CLOSE)
     reset_matrix()

run(mode=P3D)

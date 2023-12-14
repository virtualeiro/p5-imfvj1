from p5 import *
import numpy as np


cnt_x=width/2
cnt_y=height/2
max_x=width
max_y=height

     
def draw():
        
        global pos_circle
        pos_circle=[mouse_x, mouse_y]
        background(0)
        # Draw the image to the screen at coordinate (0,0)
        stroke(255,0,0)
        line((0,cnt_y), (max_x,cnt_y))
        line((cnt_x,0), (cnt_x,max_y))
        pos_circle=np.round(pos_circle,2)
        circle(pos_circle,20)
        stroke(0,255,0) 
        line((cnt_x,cnt_y),pos_circle)

        angulo = np.arctan2( cnt_y - pos_circle[1], cnt_x - pos_circle[0])
        
        angulo_em_graus=np.degrees(angulo)
        angulo_em_graus=np.round(angulo_em_graus)
        print(angulo, angulo_em_graus)
   
        stroke(0,0,255)
        push_matrix()
        translate(cnt_x,cnt_y)       
        rotate(angulo)
        begin_shape()
        vertex(0,-20)
        vertex(0,20)
        vertex(-100,0)
        end_shape(CLOSE)
        pop_matrix()
      #  if (img!=None):
      #      image(img, 0, 0)

if __name__ == '__main__':
        run()
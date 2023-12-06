from p5 import *
import numpy as numpy

v_pos=[0,100]
v_direcao=[1,0]

def setup():
    size(800,600) 

def draw():
    global v_pos
    background(255,255,255)
    
    speed=4
    v_normalized = v_direcao / np.linalg.norm(v_direcao)
    v_velocity= np.multiply(speed, v_normalized)
    v_pos=np.add(v_pos,v_velocity) 

    circle( v_pos, 40)

run()
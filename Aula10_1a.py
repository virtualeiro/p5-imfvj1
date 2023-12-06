
from p5 import *
import sys
import numpy as np 
sys.dont_write_bytecode = True

v_pos=[0,100]
v_direcao=[1,0]

def setup(): 
    size(800,600)

def draw():
    global v_pos
    background(0)
    #1- SO DIRECAO LINEAR
    v_pos=np.add(v_pos,v_direcao)
    
    circle( v_pos, 40)
run()
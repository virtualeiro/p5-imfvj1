

from p5 import *
import numpy as np
import random
v_direcao_blue=[10,10]
v_direcao_red=[0,10]

def draw():
    produto_interno=np.dot(v_direcao_blue, v_direcao_red)
    magnitude_blue=np.linalg.norm(v_direcao_blue)
    magnitude_red=np.linalg.norm(v_direcao_red)
    produto_magnitudes=np.multiply(magnitude_blue,magnitude_red)
    angulo = np.arccos(np.divide(produto_interno,produto_magnitudes))
    print(degrees(angulo))
    
run()

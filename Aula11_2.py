#VERSAO P5
"""
from p5 import *
import sys
import numpy as np 
sys.dont_write_bytecode = True

v_pos=[400,300]


def setup(): 
    size(800,600)

def draw():
    global v_pos
    background(0)
    target=[mouse_x,mouse_y]
    

    v_dir=np.subtract(target,v_pos)
    v_pos=np.add(v_pos,v_dir)
    
    circle( v_pos, 40)
run()
"""

#VERSAO PYGAME
import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))

fpsClock=pygame.time.Clock()
FPS = 15 #num segundos 
v_pos=[400,300]

while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    mouse = pygame.mouse.get_pos()
    target=[mouse[0],mouse[1]]
    v_dir=np.subtract(target,v_pos)
    v_pos=np.add(v_pos,v_dir)
    
    pygame.draw.circle( screen, (255,0,0), v_pos, 10)
        
    pygame.display.update()
    fpsClock.tick(FPS)

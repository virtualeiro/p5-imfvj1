#VERSAO P5
from p5 import *
import math

def setup():
    size(800,800)

# Parametros do spirograph 
R = 100  # Raio do circulo fixo
r = 30   # Raio do circulo móvel
d = 50   # Distancia da caneta ao centro do circulo movente 
# Calcula as coordenadas do Spirograph 
def spirograph(t):
    x = (R - r) * math.cos(t) + d * math.cos((R - r) * t / r)
    y = (R - r) * math.sin(t) - d * math.sin((R - r) * t / r)
    return int(x + width / 2), int(y + height / 2)

t = 0
def draw():
    global t
    # Obtem as coordenadas do spirograph
    spirograph_point = spirograph(t)

    # Desenha o novo ponto obtido
    fill(255,0,0)
    circle( spirograph_point, 2)

    # Actualiza o angulo para a função Spirograph 
    t += 0.01

run()    


#VERSAO PYGAME
"""
import pygame, sys
import numpy as np
import math
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Spirograph")
width=800
height=600
screen = pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

# Spirograph parameters
R = 100  # Radius of the fixed circle
r = 30   # Radius of the moving circle
d = 50   # Distance of the pen from the center of the moving circle

# Function to calculate Spirograph coordinates
def spirograph(t):
    x = (R - r) * math.cos(t) + d * math.cos((R - r) * t / r)
    y = (R - r) * math.sin(t) - d * math.sin((R - r) * t / r)
    return int(x + width / 2), int(y + height / 2)

t = 0
while True: #Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Get Spirograph coordinates
    spirograph_point = spirograph(t)

    # Draw the Spirograph point
    pygame.draw.circle(screen, (0, 0, 255), spirograph_point, 2)

    # Update the angle parameter for the Spirograph function
    t += 0.01
    
    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)
"""


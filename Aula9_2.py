from p5 import *
def setup():
    size(400, 400)
    stroke(0)
    stroke_weight(2)
    
def draw():
    background(255)
    centroX=width/2  

    for x in range(0, width):
#x - width/2 calcula a distância horizontal ao centro. 
# Se x estiver para a direita do centro, o valor é positivo, 
# Se o x estiver para a esquerda do centro, o valor é negativo.
#Colocando esse valor ao quadrado (x - width/2)**2 dá-nos valores positivos e simétricos
        
        y = 0.01 * (x - centroX)**2  # (x - centroX) traz valore x de -200 até 200
        point(x, y)

run()
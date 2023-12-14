from p5 import *

v_direcao_blue=[10,100]#Mudar aqui 
v_direcao_red=[20,-200]

resultado=0

def normaliza(v_input):
    return v_input/np.linalg.norm(v_input) 

def setup():
   global resultado
   size(400, 400)
   v_normalized1=normaliza(v_direcao_blue)
   v_normalized2=normaliza(v_direcao_red)
   resultado = np.dot(v_normalized2, v_normalized1)
def draw():
    global resultado
  
    stroke(255,0,0)
    line((width/2,height/2), (width/2+v_direcao_blue[0], height/2+v_direcao_blue[1]))
    stroke(0,0,255)
    line((width/2,height/2), (width/2+v_direcao_red[0], height/2+v_direcao_red[1]))
    
    if(resultado==1):
            print("Same Direction")
#Se o dot product for 0, 
#significa que são perpendiculares um ao outro
    elif(resultado==0): 
           print("Perpendicular")
#Finalmente se o dot.product for -1, 
#significa que ambos os vetores estão a ir em direções opostas
    elif(resultado==-1): 
           print("Opposite directions")    
    #pygame.draw.circle( screen, RED, pygame.mouse.get_pos(), 1)
    else :print("Non orthogonal nor paralell")

if __name__ == '__main__':
        run()
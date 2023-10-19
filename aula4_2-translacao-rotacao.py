from p5 import *
global ang
def setup():
        size(640, 360)

def draw():
        background(255)
        fill(0)
        circle(width/2, height/2,10)
        
        no_fill()
        #1
        
        stroke(255,0,0)
        #rotate(frame_count / 360)
        
        beginShape()
        #LADO=100
        vertex(width/2-50,height/2-50)
        vertex(width/2+50,height/2-50)
        vertex(width/2+50,height/2+50)
        vertex(width/2-50,height/2+50)
        endShape(CLOSE)
        
        #2
        
        stroke(0,0,255)
        #push_matrix()
        #....
        #pop_matrix()
        with push_matrix():
                translate(width/2, height/2)
                rotate(frame_count / 360)
                beginShape()
                LADO=100
                vertex(-50,-50)
                vertex(50,-50)
                vertex(50,50)
                vertex(-50,50)
                endShape(CLOSE)
        
        #3
        """
        stroke(0,255,0)
        with push_matrix():
                translate(width/2, height/2)
                rotate(frame_count / 360)
                figura() # Triangle
        """
def figura():
      beginShape()
      LADO=100
      vertex(-50,-50)
      vertex(50,-50)
      vertex(50,50)
      vertex(-50,50)

      endShape(CLOSE)

if __name__ == '__main__':
        run()
def setup():
    size(600, 600) 


def drawObject(x, y, s):
    push()
    translate(x, y)
    scale(s)
    fill(230) 
    ellipse(150, 150, 150, 150) 
    fill(255) 
    ellipse(120, 127, 40, 40) 
    ellipse(180, 127, 40, 40) 
    noFill()
    arc(150, 175, 40, 30, 0, PI)
    pop()
    
def draw():
    #Big Head
    drawObject(-150, -150, 3)
    #2 mini heads
    drawObject(90, 111, 0.8)
    drawObject(270, 111, 0.8)
    #4 tiny heads
    drawObject(204, 182, 0.2)
    drawObject(156, 182, 0.2)
    drawObject(384, 182, 0.2)
    drawObject(336, 182, 0.2)

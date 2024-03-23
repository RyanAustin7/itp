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
    for p in range(10):
        for k in range(10):
            drawObject(60*p-30,k*60-30,0.4)

def setup():
    size(300, 300) 

def draw():
    #Big Head Circle!
    fill(230) #Off-white
    ellipse(150, 150, 150, 150) #x, y, height, width (Just so I don't forget)
    
    #Eyes!
    fill(255) #White, might change later?
    ellipse(120, 127, 40, 40) #Left Eye
    ellipse(180, 127, 40, 40) #Right Eye
    
    #Smile!
    noFill()
    arc(150, 175, 40, 30, 0, PI)
    # Example on Processing.org: arc(105, 35, 50, 50, -PI, 0);  // upper half of circle
    

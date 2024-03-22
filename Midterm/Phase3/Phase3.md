# Phase3

## Part 1: Setup

### I decided to make my face I made in Phase2 again but larger and in the middle of a 600x600 (as opposed to my original 300x300) and fill its eyes with the same face but scaled down, since the eyes and the face itself are both perfect circles. I copied the code from my phase2 and set it up as taught in the Phase3 instructions. The resulting code looked like this:

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

### It's the same code verbatim, except with drawObject instead of draw, the pop and push functions so my second function call doesn't affect the first, and the translate and scale functions with the corresponding variables written in.

## Part 2: Calling Functions and Executing

### As I mentioned earlier, I thought it would be funny to make small scale faces and use tehm as the eyes of the big central face, so that's what I did. I ended up getting a little carried away and making 4 even tinier faces for the 2 small faces. I spent some playing with dimensions and coordinates to get them to fit exactly in the eye spots. This is what the code for that section looks like:

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

### This part was fun, and made a lot of sense.

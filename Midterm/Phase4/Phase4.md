# Phase 4

## Part 1: Setup

### I copy-pasted my phase 3 processing code into another processing file and named it phase4. I deleted all the stuff under the def draw() section to prep for the tiling print. The first thing I did was decided on doing a 10x10 smiley face print in this 600x600 grid. In order to do that, I needed the circles to be 60 pixels. They are normally 150, and to change 150 to 60 you multiply by 0.4, so I made sure to set the s variable to 0.4. Another thing I did was test where the circles are when set to (0,0,0.4). For some reason, the edge of the circles were 30 pixels positive in both the x direction and y direction, so I made sure to adjust for this in the code by adding -30 to both the x and y coordinate formulas.

## Part 2: Nested Loop

### I made the formula for a nested loop. I remembered that the outer loop counts for how many rows are printed, and the inner loop is how many objects are printed in each row. Basically the same as our pyramid assignment but slightly less complicated because we didn't need to print spaces as well. The final code ended up looking like this:

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
            drawObject(60*k-30,p*60-30,0.4)


### I chose p and k as the variables, with p being the outer loop variable to control the amount of rows and k being the inner loop controlling how many objects are printed. I set the range to 10 for both, because the scale of the 150 pixel circle is x0.4 which is 60 pixels all around, and 60x10 is 600, which is the size of the grid. I did 60xk-30 for the x coordinate, because every 60 pixels there's space for another circle, so when k is 0 it's just -30, and when k is 1 it's 30, when k is 2 it's 90, etc. And I subtracted all of these by 30 because for some reason the circle was positive 30 in both x and y directions, so there's -30 in both parts of the formula.
### The x and y formulas are the same as well because the circles are 60 pixels wide and tall, so I multiply by 60 for both.

## Challenges
### I'd say the biggest challenge for this phase was remembering how nested loops worked. I remembered the basic idea, for _ in range(__), and then within that an inner loop, for _ in range(_), and then calling a function. I just had to remember which each was doing. I messed around with the variables to see what happened, and I learned that if I changed my formula to have p in the x position and k in the y position instead of vice versa, then the outer loop controlled how many columns were there instead of rows. Ultimately it really didn't matter because it was a 10x10 grid so either would've worked, but it was a fun realization either way. That's it!

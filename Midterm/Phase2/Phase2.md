# Phase 2

## Part 1: Setup and Ellipses

### I made it so each square in the graph from phase 1 was 50 pixels, and since the smile perfectly fits in a 5x5 of squares, I set the boundaries to a 6x6, which would be (300, 300) using the example provided of

def setup():
  size(300,300)

### Then, again like the example, set up a draw function. I started with the head circle, right in the middle, with a height and width of also 150, resulting in (150,150, 150, 150). I decided to make the color a slightly off white as well to contrast the default gray background and eyes, which I made white. I did a similar thing for the eys, making them circles but smaller, in the first and second quadrants of the bigger circle. I fiddled around with the numbers to make it better match the drawing I did and to seem more normal. This is what the code lopoked like:

def draw():
    fill(230)
    ellipse(150, 150, 150, 150)

    fill(255)
    ellipse(120, 127, 40, 40) #Left Eye
    ellipse(180, 127, 40, 40) #Right Eye

### I also left in notes of formulas and colors so I wouldn't forget later when i come back to it.


## Part 2: The Curved line mouth

### This was the trickiest part to code. I went onto https://processing.org/tutorials/curves and read about arcs and curves. It seemed pretty complex, but luckily there was an example that was almost exactly what I was looking for. I found this code there:

arc(105, 35, 50, 50, -PI, 0);  // upper half of circle

### To make a smile, I wanted the lower half of a circle, and given that the formula is arc(x, y, width, height, start, stop):, I fiddled with the last 2 numbers. Since the example was -PI, 0, and that made a frown, I did (PI, 0) but that wasn't right. I kept trying other things until I found (0, PI) was the right combo. I also changed the first 4 numbers so it fit the face properly. My code resulted looking like this:

noFill()
arc(150, 175, 40, 30, 0, PI)

### I did no fill also because if it filled, it actually looked like an open mouth. It kept a straight line between the points and filled in white the arc.

### I was fine with all the stroke lines as well because it outlined the faces features. I think overall it turned out pretty well. The smile doesn't look exactly exactly like the smile on my graph but it's pretty close.  

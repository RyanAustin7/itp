### Pyramid:Fizzbuzz

## PYRAMID
 I started out doing the Pyramid code, and couldn't figure out how to get the pyramid to switch directions.
This was because I couldn't fully wrap my head around what the code was saying,
so I went to ChatGPT for some help. This is what I asked:
This is my code:
stacks = int(input("How tall would you like the pyramid (1~8)? "))

if stacks > 8:
    print("Please pick a number between 1 and 8.")
else:
    for x in range(stacks):
        for y in range(8):
            if y <= x:
                print('#', end='')
        print()

I can't figure out how to make the pyramid come out like this instead tho:
         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########

  This is the code Chat sent back to me:


  stacks = int(input("How tall would you like the pyramid (1~8)? "))

if stacks > 8:
    print("Please pick a number between 1 and 8.")
else:
    for x in range(stacks):
        for y in range(stacks - x - 1):
            print(" ", end="")
        for y in range(x + 1):
            print("#", end="")
        print()


I asked for an explanation, and chat sent this:

If stacks = 5 and y = 0 (first row):
range(stacks - y - 1) becomes range(5 - 0 - 1), which is range(4). This means the loop will iterate 4 times, printing 4 spaces.

If stacks = 5 and y = 1 (second row):
range(stacks - y - 1) becomes range(5 - 1 - 1), which is range(3). This means the loop will iterate 3 times, printing 3 spaces.

This Helped make everything more clear, as I then understood what was happening. Y would increase from 0 to 7 each time and that would affect the calculations, either printing a space or #.

~~~~~~~~~~

## FIZZBUZZ

This one was much easier for me to understand. My code was:

for index in range(0, 100, 1):
    if index % 3 == 0 and index % 5 == 0:
        print("fizzbuzz")
    elif index % 3 == 0:
        print ("fizz")
    elif index % 5 == 0:
        print ("buzz")
    else:
        print (index)

I used elif statements to work downwards, starting with things that were divisible by both 3 and 5, and having the result print FizzBuzz.
I then did the same thing for things divisible by only 3 or only 5, with the appropriate results to follow.

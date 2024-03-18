# Power Markdown File

## Part 1
I was a little stumped at first making this.
I thought in order to make the graph exactly as it's listed, all I needed to do was make a variable i in range of -8 to 9 (because it really goes to 8),
and then make another variable which I just called length equal to i squared, which is i ** 2 because two asterisks is raising something to the power of the next number.
Then I would print an asterisk * times the variable length, so it would go from -8 to 8 and square them all. This is what the final code looked like:
 def print_graph():
     for i in range(-8, 9):
         length = i ** 2
         print("*" * length)
 print_graph()
This printed the graph exactly as it's listed on the site, but then I wanted to have someone input a number and have that be equal to the variable i that I made, so I tried again.

## Part 2
I commented the first attempt out but wanted to keep it there just in case.
For my second attempt, I started out by making an integer input like we've done before in class, where you can input a number between -8 and 8.
I set this number to be variable x. Then I wrote if -8 <= x <= 8, for i in range (-x, x+1) and the +1 this is the same logic as before, where I wrote -8 to 9 instead of -8 to 8 to account for an accurate upper limit.
Then I would have it print * times (i**2). So this accomplishes the same thing as the first attempt, but you can pick a number up to 8 as opposed to the output always being 8 ** 2.
My final code looks like this:
x = int(input("Pick a number between -8 and 8: "))

if -8 <= x <= 8:
    for i in range(-x, x + 1):
        print("*" * (i ** 2))
else:
    print("The number must be between -8 and 8.")

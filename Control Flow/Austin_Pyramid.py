stacks = int(input("How tall would you like the pyramid (1~8)? "))

if stacks > 8:
    print("Please pick a number between 1 and 8.")
else:
    for y in range(stacks):
        for x in range(stacks - y - 1):
            print(" ", end="")
        for x in range(y + 1):
            print("#", end="")
        print()

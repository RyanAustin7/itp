# def print_graph():
    # for i in range(-8, 9):
        # length = i ** 2
        # print("*" * length)
# print_graph()


x = int(input("Pick a number between -8 and 8: "))

if -8 <= x <= 8:
    for i in range(-x, x + 1):
        print("*" * (i ** 2))
else:
    print("The number must be between -8 and 8.")
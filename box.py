for x in range(5):
    for y in range(5):
        if x + y == 4 or x == 4 or y == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()
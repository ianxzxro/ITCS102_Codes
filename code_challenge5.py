n = int(input("Enter value of x >"))
for x in range(n):
    for y in range(n):
        if x + y == n-1 or x - y == 0:
            print("*", end="")
        else:
            print(" ",end="")
    print()

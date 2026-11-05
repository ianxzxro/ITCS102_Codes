IsHungry = True

while IsHungry:
    x = bool(input("Are you hungry? (True/False): "))
    if x == True:
        print("You should eat something!")
        continue
    else:
        print("You should wait for lunch")
        break

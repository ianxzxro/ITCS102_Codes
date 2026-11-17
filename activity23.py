#JEEPNEY SIMULATION

route = ["SM", "Pacific Mall", "DLL"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True :
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("1 Sakay 2 Priority seat 3 Para po!")
    print("4 Sa Kanto Lang 5 Sa Tabi Lang")
    print("6 Seat Check 7 Balikan 8 Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("Puno na!")
        else:
            name = input("NAME: ")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passengers) == SEATS:
            print("Puno na!")
        else:
            name = input("NAME: ")
            passengers.insert(0,name)
            total = total + FARE
            print(name, "took the priority seat.")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off. Babye!")
        else:
            print(name, "is not on this jeep")

    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            kanto = passengers.pop()
            print(kanto, "got of at the kanto.")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            tabi = passengers.pop()
            print(tabi, "got of at the tabi.")

    elif choice == "6":
        for x in range(len(passengers)):
            print("Seat", x + 1, passengers[x])

    elif choice == "7":
        route.reverse()
        print("Route:", route)

    elif choice == "8":
        print("Total fare today:", total)

    else:
        print("Invalid")

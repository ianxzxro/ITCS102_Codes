anime_type = ["isekai", "adventure", "drama", "action"]
anime_title = []

while True :
    ans = input("Do you know any Anime -- (Yes/No)")

    if ans.lower() == "yes" :
        print("What is its type -- ? select from the list ")
        for x in anime_type :
            print(x)

        anime_type = input("Type --> ")


        title = input("What is the title of the anime? ")
        anime_title.append(title)
        continue
    else :
        print("Thank you")
        break 
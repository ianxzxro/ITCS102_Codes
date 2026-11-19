fruits = ["mango", "apple", "banana", "orange", "mangosteen"]
#dictionary
#key, value
fruits_d = {"gren":"mango", "rid":"apple","yilo":"banana","orins":"orange","purpol":"mangosteen"}

print(fruits_d["gren"])

#traversing a dictionary

for x,y in fruits_d.items():
    print("key is =",x,"value is =",y)
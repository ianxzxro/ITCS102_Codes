# Write a program that calculates total shipping charges using package details, location rules, and strict conditional order.|

sender_name = input("ENTER SENDER NAME --->  ")
item_type = input("ITEM --->  ")
is_fragile = input("Is the Item Fragile? (True or False) ---> ") == True
weight = float(input("What is the weight(kg) ---> "))
distance = float(input("What is the distance(km) ---> "))
is_express = input("Is it Express? (True or False) ---> ") == True
is_international = input("Is it International? (True or False) ---> ") == True

#calculate the base cost
base_cost = (weight * 2.50) + (distance * 0.15)

#evaluate pricing tiers
if weight <= 2.0 and distance <= 100.0 and not is_express and not is_international:
	total = 0.00

elif is_international and is_express:
	total = (base_cost * 1.40) + 50

elif is_express or is_international :
	total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000 :
	total = base_cost + 30

else:
	total = base_cost

print("--- YOUR ORDER ---")
print("NAME OF SENDER:", sender_name)
print("TYPE OF ITEM:", item_type)
print("FRAGILE:", is_fragile)
print("WEIGHT:", weight)
print("DISTANCE:", distance)
print("EXPRESS/NOT EXPRESS:", is_express)
print("INTERNATI0NAL/NOT INTERNATIONAL:", is_express)
print("TOTAL SHIPPING COST --->$", total)


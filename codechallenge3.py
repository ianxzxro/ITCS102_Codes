# Write a program that calculates total shipping charges using package details, location rules, and strict conditional order.|

name = input("NAME --->  ")
type = input("ITEM --->  ")
is_fragile = bool(input("Is the Item Fragile?"))
weight = float(input("What is the weigth?"))
distance = float(input("What is the distance?"))
is_express = bool(input("Is it Rush?"))
is_international = bool(input("Is it International?"))
base_cost = input(weight * 2.50) + (distance * 0.15)

if is_fragile == True:
	print("Handle it safely")
else : 
	print("Package it well")
if weight <= 2.0 and distance <= 100.0 and is_express == False or is_international == False :
	print("Free Shipping ($0.00)")
else :
	print("$","base_cost")



#conditional statement/selection statement

import getpass

username = 'user1'
password = 'nagingakoba?'

u = input("Enter Username ---->  ")
p = getpass.getpass("Enter Password ---->  ")

if username == u and password == p :
	print("OO")
else:
	print("HINDI WAG KA MAG ASSUME")
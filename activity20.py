from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "pogi" and password == "akonato":
        print("Yes!")
        isLogin = True
    else:
        print("No!")
        
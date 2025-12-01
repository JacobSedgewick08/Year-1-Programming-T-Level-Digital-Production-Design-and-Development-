counter = 1
while counter <=3:
    username = input("Please enter the username")
    password = input("Please enter the password")
    if username == "DanDruff" and password == "Shampoo":
        print("Access Granted")
        break
    else:
        print("Access Denied, Try again")
        counter = counter + 1

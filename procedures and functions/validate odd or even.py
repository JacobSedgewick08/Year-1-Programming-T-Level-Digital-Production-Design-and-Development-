def validation():
    num=int(input("Please enter a number: "))
    if num % 2 == 0:
        print(num, "is even")
    elif num % 2 == 1: 
        print(num, "is odd")    
    else:
        print("You havent entered a number")

validation()
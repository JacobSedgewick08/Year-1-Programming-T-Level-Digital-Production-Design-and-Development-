def add(a,b):
    return(a+b)

def subtract(a, b):
    return(a-b)

def multiply(a, b):
    return(a*b)

def division(a, b):
    return(a/b)

menu=int(input("Welcome to the menu would you like to\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n"))
a=int(input("Please enter a number"))
b=int(input("Please enter another number"))

if menu == 1:
    print(add(a, b))

if menu == 2:
    print(subtract(a, b))

if menu == 3:
    print(multiply(a, b))

if menu == 4:
    print(division(a, b))


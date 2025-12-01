print("1. Input a grade")
print("2. View the grades")
print("3. Exit")
which=int(input("Please enter the number of the action you would like to do"))
if which==1:
    f = open("project", "a")
    student = input("Would you like to enter a student")
    while student=="yes":
        name=input("What is the students name")
        grade=input("What is the students grade")
        f.write(name)
        f.write(grade)
        student=input("Would you like to enter another student")
        if student=="no":
            print("Thank you for using the program")

if which==2:
    f = open("project", "r")
    print(f.read())

if which==3:
    exit
          
          
    

print("1. Input a Grade")
print("2. View the grades")
print("3. Exit")
which=int(input("Please enter the number of the action you would like to do"))
if which==1:
    f = open("project", "a")
    student = input("Would you like to enter a student")
    while student=="yes":
        name=input("What is the students name")
        grade=(input("What grade did they get ?"))
        f.write(name)
        f.write(grade)
        student = input("Would you like to enter another student")
        if student=="no":
            print("Thank you for using the grade calculator")

if which==2:
    f = open("project", "r")
    print(f.read())
        
if which==3:
    exit

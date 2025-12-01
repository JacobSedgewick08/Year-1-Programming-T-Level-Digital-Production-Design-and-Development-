file = open("addbook.csv","r")
line = file.readline()
number=int(input("Please enter a number between 1 and 3"))

if number == 1: 
    City=input("Which city do they live in ? ")
    if City==data[1]:
        print("Name: ",data[0])
        print("Town: ",data[1])
        print("Adress: ",data[2])
        print("Phone Number: ",data[3])
    
if number == 2:
    Adress=input("What is their adress")
    while(line):
        data=line.split(",")
        if Adress==data[2]:
            print("Name: ",data[0])
            print("Town: ",data[1])
            print("Adress: ",data[2])
            print("Phone Number: ",data[3])

if number == 3:
    Phone=(input("What is their phone number"))
    while(line):
        data=line.split(",")
        if Phone==data[3]:
            print("Name: ",data[0])
            print("Town: ",data[1])
            print("Adress: ",data[2])
            print("Phone Number: ",data[3])
        line=file.readline()
file.close


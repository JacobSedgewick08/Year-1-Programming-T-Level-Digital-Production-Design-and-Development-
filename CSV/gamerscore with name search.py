file = open("gamerscore.csv", "r")
line = file.readline()
Searchname = input("Please enter a name: ")

while(line):
    data = line.split(",")
    if data[0]==Searchname:
        print("Handle: ",data[0])
        print("Gamerscore: ",data[1])
    if data[0] !=Searchname:
        print("This user is not in the list")
    line=file.readline()

file.close()

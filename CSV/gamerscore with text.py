file = open("gamerscore.csv", "r")
line = file.readline()

while(line):
    data = line.split(",")
    print("Handle: ",data[0])
    print("Gamerscore: ",data[1])
    line=file.readline()

file.close()

inputFile = open("inputFile.txt","r")
#print(inputFile.read())   # To read all the file given
# to get only pass values
for line in inputFile:
    line_split= line.split()
    if line_split[2] == "P":
        print(line)
inputFile.close()
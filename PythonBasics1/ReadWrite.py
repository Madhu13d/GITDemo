file = open('test.txt')
#Read() will help to read all the contents of file
#print(file.read())# prints all the data from the text file
#print(file.read(2))# read number of characters which is provided as parameter
#line= file.readline() # reads one single line at a time
#while line!="":
#    print(line)
 #   line = file.readline()
#print("&&&&&&&&&&&&&&&")
#redlines() will read all the data in he text file and store them in the List.
# Iterate through the List to retrieve the data
for line in file.readlines():
    print(line)

file.close()
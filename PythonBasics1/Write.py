#read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)# will reverse all the data in the content
    with open('test.txt','w')as writer:
        for line in reversed(content):
            writer.write(line)
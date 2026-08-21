#Example1: Write in file

# file = open("C:/Users/Megha Kadam/Downloads/prashant.doc",'w')
# file.write("This is first line...\n")
# file.write("This is second line...\n")
# file.write("This is third line...\n")
# file.close()
# print("Program completed...")
# file.close()


#Example2: Read data in file
# file = open("C:/Users/Megha Kadam/Downloads/prashant.doc",'r')
# #print(file.read())
# print(file.readline())
# file.close()

#Example3: Append text in file

file = open("C:/Users/Megha Kadam/Downloads/prashant",'a')
file.write("This is forth line...\n")
file.write("This is fifth line...\n")
#print(file.read())     #io.UnsupportedOperation: not readable
file.close()
print("Program completed...")
file = open("C:/Users/Megha Kadam/Downloads/prashant",'r')
print(file.read())
file.close()


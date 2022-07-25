'''
Used to handle a file operations
like:
   Opening,Closing,Reading,Writing,Appending,Looping
Before reading/writing , we need to open a file
    f=open(fileName,mode)
After reading / wrirting need to close a file
   f.close() where f is a file pointer
r--> open files for read only
w--> open files for write only
a-->open files for append only
'''
print("---------------")
print("Writing a data to file")
file =open("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\python\\DemoFile.txt",'w')#Opens file for writing
file.write("Dhoni is my Inspiration\n") #\n command to be used print in next line
file.write("Dad is great\n")
file.close()
print("File written successfully")


print("---------------")
print("Reading a data from file")
#(read[number]) read specified number chars from file
#readline() read nect line entire contents in file
#readlines() read lines of strings
file = open("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\python\\DemoFile.txt",'r')
#print(file.read()) #return entire contents
#print(file.readlines()) #returns as it is like we entered
#print(file.readline(2)) #returns char length from a line
print(file.readline()) #returns first line
file.close()


print("---------------")
print("Appending a data to file")
file = open("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\python\\DemoFile.txt",'a')
file.write("Always be happy\n")
file.close()

print("---------------")
print(" Looping a data from file")
file = open("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\python\\DemoFile.txt",'r')
for l in file:
    print(l)
file.close()
file=open("testfile.txt","w")

file.write("Hello World\n")
file.write("My name is Raissa\n")
file.write("I'm 18 years old\n")
file.write("And i'm engaged to Prestige")

file.close()

file=open("testfile.txt","r")
print(file.read())
file.close()

print()

file=open("testfile.txt","r")
print(file.read(5))
file.close()
print()

file=open("testfile.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print()
print()

file=open("testfile.txt","r")
print(file.readlines()[3])
file.close()

print()

#To add and print phrase in a file using a for loop
file=open("testfile.txt","r")
for line in file:
    print(line,end='')
file.close()

print()
print()

#To add a phrase in a list without modifying the 1st program
file=open("testfile.txt","a")
file.write("\nCan't wait to be his wife")
file.close()

file=open("testfile.txt","r")
print(file.read())
file.close()


#To add a list of phrases withoit modifying the 1st program

print()
print()

file=open("testfile.txt","a")
line_of_text=["\nI'd like to add that starting from 21st of October\n","I started a new life\n","Now i know what i want for myself and for my life\n","I've never been so sure and so determined for my future.\n"]
print(file.writelines(line_of_text))
file.close()

file=open("testfile.txt","r")
print(file.read())
file.close()


#When the file containes images or videos


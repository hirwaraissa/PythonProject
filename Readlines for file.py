file=open("testfile.txt","w")

file.write("Hello World\n")
file.write("My name is Raissa\n")
file.write("I'm 18 years old\n")
file.write("And i'm engaged to Prestige")

file.close()

file=open("testfile.txt","r")
for i in range (2):
    print(file.readline())
    
print(len(file))
file.close()
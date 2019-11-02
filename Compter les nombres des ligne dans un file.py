file=open("Essay.txt","w")
file.write("Hi!My name is Raissa\n")
file.write("I'm 18 years old\n")
file.write("And i'm in love with Prestige Alain\n")
file.write("He's in master 1 and lies in Liège\n")
file.write("I really love this boy...He's my everything!\n")
file.close()



filename=open("Essay.txt","r")
filename.read()



def line_count(filename):
    count=0
    with open("Essay.txt","r") as filename:
        for line in filename.readlines():
            count+=1
        
    return count
    

def char_count(filename):
    c=0
    with open("Essay.txt","r") as filename:
        for line in filename.readlines():
            for char in line:
                c+=1
        
    return c

def space(filename,n):
    with open("filename.txt","w") as filename:
        for i in range(n):
            filename.write("\n")
                  
    return

filename_in=open("filename_in.txt","w")
filename_in.write("my name is raissa!")

filename_out=open("filename_in.txt","w")

def capitalizeMine(filename_in,filename_out):
    with open("filename_in.txt","w") as filename_in:
        filename_in.write("my name is raissa!")
    with open("filename_in.txt","r") as filename_in:
        for line in filename_in:
            with open("filename_out.txt","w") as filename_out:
                filename_out.write(line.upper())
                
def capitalize(filename_in,filename_out):
    file_in=open("filename_in","r")
    file_out=open("filename_out","w")
    for line in file_in:
        file_out.write(line.upper())
    file_in.close()
    file_out.close()
    

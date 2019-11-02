filename=input("Entrez le nom du ficher(avec.txt): ")
try:
    with open(filename,"r") as file:
        count=0
        ligne=0
        for e in file.read():
            count+=1
    with open(filename,"r") as file:
        for i in file.readlines():
            ligne+=1
            
    print(count)
    print(ligne)
except:
    print("There is no file named ", filename)
    filename=input("Réentrez un nouveau nom du ficher(avec.txt): ")
    try:
        with open(filename,"r") as file:
            count=0
            ligne=0
            for e in file.read():
                count+=1
        with open(filename,"r") as file:
            for i in file.readlines():
                ligne+=1
            
        print(count)
        print(ligne)
    except:
        print("There is no file named ", filename)
    

def binary_search (name,filename):
    #print("the file name to open is:",filename)
    with open(filename,"r") as file:
        count=0
        
        lines = file.readlines() #list that will contain all read lines
        #sorted_list=lines.sort() #list that will contain all sorted lines
        lines.split(',')
        print(lines)
    with open(filename,"r") as file:
        first = 0
        last = len(lines)-1
        found = False
        while first<=last and not found:
            middle = (first + last)//2
            #print(lines[middle] , "?=" , name)
            if lines[middle] == name:
                found = True
            else:
                if name < lines[middle]:
                    last = middle-1
                else:
                    first = middle+1
    return found  
try:
    with open(filename,"r") as file:
        name=input("Entrez le mot: ")
        
    with open(filename,"r") as file:
        binary_search (name,filename)
        if found==True:
            
            print("Search found ")
        else:
            print("Search was not found ")
except:
    print("There isn't any ",name)
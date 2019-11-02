av=[("Palmina",(45,21)),("Raissa",(18,2001)),("Alain",(20,4)),("Vany",(24,5))]

def coordinate(commune,all_communes):
    first = 0
    last = len(all_communes)-1
    found = False
    
    while first<=last and not found:
        middle = (first + last)//2
        cm, cordi = all_communes[middle]
        if cm== commune:
            return True
            
        else:
            if commune < cm:
                last = middle-1
            else:
                first = middle+1
    return False        

name,cordinates = av[0]

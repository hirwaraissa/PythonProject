
def is_adn(s):
    check = ['a','A','t','T','g','G','c','C']
    for char_ in s:
        if char_ in check:
            pass
        else:
            return False
    return True

def position(s,p):
    
    print(list(enumerate(s)))
    print(list(enumerate(p)))

        
def distance_h(s,p):        #If the string s is different from the string p, compare each letter in s to each letter in p, and if there is a difference, the variable distance will be added 1 and if not , pass .
    distance=0
    
    if len(s)==len(p) and s!=p:
         for i in s:
             if i in p:
                 pass
             else:
                 distance+=1
         
        
    if len(s)!=len(p):
        distance=None
    print(distance)
        
  
def distance_matrice(l):  #la fonction va prendre un caractère dans la chaine de caractere l, puis la comparer avec tous les autres caractere dans la meme list + lui meme
    distance=0
    s=[]
    for i in l:
        if len(l[0])!=len(l[1]):
            distance=None
            s.append=distance

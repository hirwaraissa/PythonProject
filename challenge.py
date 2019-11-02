n= int(input("Entrez la valeur du coefficient n : "))
min= int(input("Entrez la valeur minimale pour a, b, c et d: "))

for a in range(1,min):
    for b in range(1,min):
        for c in range(1,min):
            for d in range(1,min):
                if a**n + b**n == c**n + d**n:
                    print("a =", a, " b =", b, " c =",c, "d =",d)
                    
                    
                    
                

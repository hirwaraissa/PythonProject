solutions = 0
a = input("Entrez la valeur du coefficient a : ")
b = input("Entrez la valeur du coefficient b : ")
c = input("Entrez la valeur du coefficient c : ")
max = int(input("Entrez la valeur maximale pour x, y et z: "))

for x in range(1,max):
    for y in range(1,max):
        for z in range(1,max):
            if x**a + y**b == z**c:
                print("x =", x, " y =", y, " z =",z)
                solutions += 1

if solutions == 0:
    print("Aucune solution trouvee")
else:
    print(solutions, "solutions trouvees") 
    
    
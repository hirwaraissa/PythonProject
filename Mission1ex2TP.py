found=False
borne=int(input("Entrez la borne maximale de recherche: "))
borne_diviseur=int(input("Combien de diviseur prope doit avoir le nombre: "))

for i in range(1,borne+1):
    compt=1
    for j in range(2,i//2+1):
        if i%j==0:
            compt+=1
    if compt==borne_diviseur:
        print(i,"a",borne_diviseur,"diviseurs")
        found=True
        break
if found==False:
    print("aucun nombre n'a", borne_diviseur,"diviseurs")
        
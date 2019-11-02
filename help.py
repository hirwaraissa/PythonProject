carac=str("X")
hauteur=int(input("Entrez une hauteur: "))

def croix(carac,hauteur):
    """ pré: h>0,carac
        post: afficher une croix de hauterur hauteur et de caractere carac
    """
    for n in range(hauteur):
        for m in range(hauteur):
            if n!= hauteur//2:
                if m==hauteur//2:
                    print(carac,end="")
                else:
                    print(" ",end="")
            else:
                print(caract,end="")
        print()
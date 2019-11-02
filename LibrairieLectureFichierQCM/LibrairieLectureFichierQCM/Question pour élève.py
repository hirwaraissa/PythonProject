import qcm
import random
rng=random.random()

"""Questions pour les étudiants.
Donc la correction et le commentaire du prof ne sont pas afficher"""

if __name__ == '__main__':
    filename = "QCM3.txt"
    
    
    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    print("Bienvenue.")
    for q in (int(len(questions))):
        print("\tQuestion " + str(q+1) + ": \"" + rng.randrange(questions[q][0]) + "\"")
        for r in range(4):
            print("\t\tReponses " + str(r+1) + ":" +questions[q][1][r][0])
        enregistrement=int(input("Entrez votre réponse: "))
        if enregistrement>4 or enregistrement<0:
            print("Erreur! Entrez une réponse existente!")
            print("Reentrez une nouvelle réponse: ")
        
    print("Merci pour vos réponses!")
    
            

import qcm
"""Questions pour les étudiants.
Donc la correction et le commentaire du prof ne sont pas afficher"""

if __name__ == '__main__':
    filename = "QCM3.txt"
    
    
    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    print("Bienvenue.")
    for q in range(len(questions)):
        print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")
        for r in range(4):
            print("\t\tReponses " + str(r+1) + ":" + questions[q][1][r][0])
        enregistrement=int(input("Entrez votre réponse: "))  
            
          

            
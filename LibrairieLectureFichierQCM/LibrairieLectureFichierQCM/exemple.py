import qcm

"""
    Exemple d'utilisation de la librairie de lecture de fichiers QCM
"""


if __name__ == '__main__':
    filename = "QCM3.txt"

    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    
    print("Mon propre QCM.")
    for q in range(len(questions)):
        print("\tQuestion " + str(q+1) + ": \"" + questions[q][0] + "\"")
        for r in range(len(questions[q])):
            print("\t\tReponses " + str(r+1) + ":")
            print("\t\t\tMessage: \"" + questions[q][1][r][0] + "\"")
            print("\t\t\tCorrect: " + str(questions[q][1][r][1]))
            print("\t\t\tFeedback: \"" + questions[q][1][r][2] + "\"")


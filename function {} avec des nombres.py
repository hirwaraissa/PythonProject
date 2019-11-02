n1 = "Paris"
n2 = "Whitney"
n3 = "Hilton"


print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||"
        .format(n1,n2,n3,1981))
# Le < met le string au debut d'une ligne, le ^ met le string au milieu de l'endroit proposé et le > met le string
#à la fin de la ligne.


print("|||{0:>15}|||{1:^15}|||{2:<15}|||Born in {3}|||"
        .format(n1,n2,n3,1981))

print("The decimal value {0} converts to hex value {0:x}"
        .format(123456))

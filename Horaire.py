import calendar

cal=calendar.month(2019, 10)

print(cal)

a=str(input('Entrez le jour: '))
for i in ['Mo', 'Tu', 'We','Th','Fr','Sa','Su']:
    if str(a) == str(i):
        b=int(input('Entrez la date: '))
        if b>31:
            print("Impossible car 30 jours dans un mois")
        else:
            c=float(input("Entrez l'heure: "))
            if c>24:
                print("Impossible car 24H dans une journée")
            else :
                print("Disponible")
                quit()
print('Jour pas defini')


    


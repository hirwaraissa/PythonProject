e=int(input("Entrez un nombre: "))
n=int(input("Entrez le nombre max: "))

for i in range(1,n+1):
    if e%i==0:
        print(i)
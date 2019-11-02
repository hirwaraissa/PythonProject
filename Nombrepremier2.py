n=int(input("Votre nombre: "))
premier=True
k=2
while k<n and premier:
    if n%k==0:
        premier=False
    k+=1
    
if premier:
    premier(n,"premier")
else:
    print(n,"pas premier")
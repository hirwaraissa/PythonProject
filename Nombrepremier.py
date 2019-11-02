n=int(input("votre nombre: "))
premier=True
for k in range(2,n):
    if n%k==0:
        premier=False
if premier:
    print(n,"premier")
else :
    print(n, "pas premier")
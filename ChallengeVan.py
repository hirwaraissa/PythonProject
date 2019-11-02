u=input("Entrez votre nom d'utilisateur: ")#username
p=input("Entrez votre mot de passe: " )#password
v=input("Reentrez votre mot de passe: ")#verification
z=int(2019)#security code
if v==p:
     print("Welcome")
else :
     code=int(input("Entrez votre code de securité: "))
     if code==z:
         print("Welcome")
     else :
         print("Vous n'avez pas droit d'utiliser ce compte")
 
  
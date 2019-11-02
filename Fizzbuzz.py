i=int(input(""))
temp=0
if i>=1:
    if i%3==0:
        temp="fizz"
    if i%5==0:
        temp="buzz"
    if i%3==0 and i%5==0:
        temp="fizzbuzz"
    if i%5!=0 and i%3!=0:
        temp="no"
    print(temp)
        
#def interests(base,y,x):
 #   print("Le solde sera de ",base*(1+y/100)**x)
def interests(base,y,x):
    solde=0
    if x>=0:
        solde=base*(1+y/100)**x
    return solde

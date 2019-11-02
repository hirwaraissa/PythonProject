n=int(input(""))
is_prime=True
count=0
i=1
while i<=n :
    if n%i==0:
        count+=1
    i+=1
if count>2:
    is_prime=False
print(is_prime)


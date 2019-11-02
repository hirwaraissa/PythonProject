n=int(input(" "))
sum=0
count=0
for x in range (1,n**2):
    while count<=n:
        if x%2==0:
            count+=1
            sum=sum+x      
print(sum)


while count<=n:
    for x in range (1,n**2):
        if x%2==0:
            count+=1
            sum=sum+x
print(sum)
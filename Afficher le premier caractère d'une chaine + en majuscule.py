l = "louvain-la-neuve" 
print(l[3])
print(l[-1])
print(l[-16])
print(l[0].upper())
print(l[1:15])
print(l[1:])
print(l[0].upper()+l[1:])


indices=[]
for i in range(len(l)):
    if l[i]=="_":
        indices.append(i)
print(indices)


indices=[]
for i in range(len(l)):
    if l[i]=="_":
        print(l[:i])
        break
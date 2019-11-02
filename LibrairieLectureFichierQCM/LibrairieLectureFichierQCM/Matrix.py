matrix=[]
for i in range (2):
    row=[]
    for i in range (4):
        row.append(0.0)
        
    matrix.append(row)
print(matrix)



l=[]
for i in range (4):
    s=[]
    for i in range (2):
        s.append(i)
    
    l.append(s)
print(l)




m=[]
for i in range (4):
    n=[]
    for i in range (3):
        p=[]
        for i in range (2):
            p.append(i)
        n.append(p)
    m.append(n)
        
    
    
print(m)
print(m[0][1])

l=[12,24,0,4]
s=[]
for i in l:
    for r in l:
        if i<=r:
            pass
        else:
            a=i
            i=r
            r=a
            s.append(r)
            
        
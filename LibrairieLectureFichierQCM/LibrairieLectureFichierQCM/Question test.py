def ntimes(l1,l2):
    T=0
    for e in range(len(l1)):
        for i in range (len(l2)-1):
            if l1[e]==l2[i] and l1[e+1]==l2[i+1]:
                T+=1
    return T

l = [12,24,0,4,8,1,9]

def minima(l):
    for i in l:
        count = 0
        for m in l:
            if i <= m:
                count = count + 1
        if count == len(l):
            minima = i
            l.remove(i)
    return minima
               
s=[]
for i in range(len(l)):
    s.append(minima(l))

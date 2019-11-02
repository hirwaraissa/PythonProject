def count(event, i, j):
    c=0
    for k in zip (i,j):
        if k==event:
            c+=1
    return c




def sum(x):
    """
    pré: x >0
    post:sommet
    """
    result=0
    for i in range(1,x+1):
        result=result+i
    return result
print(sum(10))
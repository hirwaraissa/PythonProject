def is_correct(PRNG):
    """pré: La graine est 33 et la periode est de 11
       post:Le PRNG commence par 33 est fait un calcul pour faire apparaitre un nombre aléatoire.
       """
    prng=PRNG(33,11)
    s=[]
    for i in range(11):
        s.append=prng.next_int(33)
    l=[]
    for y in range(11):
        l.append=prng.next_int(33)
    if prng.next_int[i]==prng.next_int[y]:
        return False
    return True
    
    
    prng=PRNG(3,11)
    s=[]
    for i in range(11):
        s.append=prng.next_int(3)
    l=[]
    for y in range(11):
        l.append=prng.next_int(3)
    if prng.next_int[i]==prng.next_int[y]:
        return False
    return True
    
    
    
    prng=PRNG(5,11)
    s=[]
    for i in range(11):
        s.append=prng.next_int(5)
    l=[]
    for y in range(11):
        l.append=prng.next_int(5)
    if prng.next_int[i]==prng.next_int[y]:
        return False
    return True


    prng=PRNG(11,11)
    s=[]
    for i in range(11):
        s.append=prng.next_int(11)
    l=[]
    for y in range(11):
        l.append=prng.next_int(11)
    if prng.next_int[i]==prng.next_int[y]:
        return False
    return True
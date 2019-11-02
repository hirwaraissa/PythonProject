def is_correct(PRNG):
    s=[]
    
    for z in range (11):
        
        prng.next_int()
        
    l=[]
    for y in range(11):
        
        prng.next_int()
        
    for i in s:
        if prng.next_int(l)==prng.next_int(s):
            return False
    return True
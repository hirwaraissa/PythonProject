def primes(max):
    prime=[]
    for i in range (2,max+1):
        status=True
        for j in prime:
            if i%j==0:
                status=False
        if status:
            prime.append(i)
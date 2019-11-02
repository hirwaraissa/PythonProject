def greatest_divisor(a):
    gd=0
    for i in range(2,100000):
        if a%i==0:
            if i==a:
                pass
            else:
                gd=i
            
    print(gd)
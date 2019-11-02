import math 


def syracuse(n):
    if n%2==0:
        R=n//2
    else:
        R=3*n+1
    return R

def syracuse10(n):
    for i in range(10):
        n=syracuse(n)
        print(n)

def vol_syracuse(n):
    while n!=1:
        n=syracuse(n)
        print(n)

def graphe_vol(n):
    i=0
    while n!=1:
        n=syracuse(n)
        i=i+1
        plot(i,n,"ro")
    show()

def temps_vol(n):
    t=0
    while n!=1:
        t=t+1
        n=syracuse(n)
    return t

def graphe_temps():
    plot(1,1,"ro")
    for i in range(2,100):
        t=temps_vol(i)
        plot(i,t,"ro")
    show()

def recherche():
    M=1
    T=1
    for i in range(2,100):
        t=temps_vol(i)
        if t>T:
            M=i
            T=t
    return M,T


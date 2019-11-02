def test_premier(n):
    for k in range (2,n):
        if n%k==0:
            print(n,"pas premier")
            return
        print(n,"premier")
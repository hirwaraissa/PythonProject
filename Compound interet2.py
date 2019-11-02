def final_amt(p, r, n, t):
    """
      Apply the compound interest formula to p
       to produce the final amount.
    """

    a = p * (1 + r/100) ** (n*t)
    return a         # This is new, and makes the function fruitful.

# now that we have the function above, let us call it.
p=int(input("How much do you want to invest?: "))
r=float(input("How much percent do you gain?: "))
n=float(input("How many times?: "))
t=float(input("for how many years?: "))
fnl=final_amt(p,r,n,t)
print("At the end of the period you'll have", fnl)
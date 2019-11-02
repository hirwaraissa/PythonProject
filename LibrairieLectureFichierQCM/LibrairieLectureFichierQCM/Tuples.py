tup=(5,)
print(type(tup))
print()
Raissa=("Hirwa",18,"Kacyiru",12,9,"Black")
print(Raissa[3])
print()
Raissa=("Hirwa",18,"Kacyiru",12,9,"Black") + ("Red","White")
print(Raissa)
print()

a=("Hirwa",18,"Kacyiru",12,9,"Black")
(name,age,b_place,b_day,b_month,color)=a

print(name)
print(color)
print(b_place)
print()
print()

julia_more_info = ( ("Julia", "Roberts"), (8, "October", 1967),
                     "Actress", ("Atlanta", "Georgia"),
                     [ ("Duplicity", 2009),
                       ("Notting Hill", 1999),
                       ("Pretty Woman", 1990),
                       ("Erin Brockovich", 2000),
                       ("Eat Pray Love", 2010),
                       ("Mona Lisa Smile", 2003),
                       ("Oceans Twelve", 2004) ])
print(julia_more_info[4][4])

print()
print()

xs = [1, 2, 3, 4, 5]

for (i, val) in enumerate(xs): #enumerate=len
    xs[i] = val**2
print(xs)
print()
print()

for (i, v) in enumerate(["banana", "apple", "pear", "lemon","Mango"]):
     print(i, v)
print()
print()
xs = [1, 2, 3, 4, 5]
ys = [3, 4, 5, 6, 7]


for x, y in zip(xs,ys): #Makes a tuple
    print (x,y)
    
print()
print()

xs = [1, 2, 3, 4, 5]
ys = [3, 4, 5, 6, 7]


for i, (x, y) in enumerate(zip(xs,ys)): #???????????????????????????????????????????
    xs[i] = x**2
    ys[i] = y**2
    print(xs,ys)
    
print()
print()
print()
    
####Creation d'un tuple###
    
r=[]
for i in range(5):
    r.append(i)
r=tuple(r)
print(r)
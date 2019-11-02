#print("i\ti**2\ti**3\ti**5\ti**10\ti**20") This is when i write without the string formatting
#for i in range(1, 11):
#    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t",i**10, "\t", i**20)
#The script above prints this:
#
#i       i**2    i**3    i**5    i**10   i**20
#1       1       1       1       1       1
#2       4       8       32      1024    1048576
#3       9       27      243     59049   3486784401
#4       16      64      1024    1048576         1099511627776
#5       25      125     3125    9765625         95367431640625
#6       36      216     7776    60466176        3656158440062976
#7       49      343     16807   282475249       79792266297612001
#8       64      512     32768   1073741824      1152921504606846976
#9       81      729     59049   3486784401      12157665459056928801
#10      100     1000    100000  10000000000     100000000000000000000
# As you can see the last colon isn't perfect, doesn't align as i want, so to do, i must use the string formatting
#in order to really align everything.

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))
    


layout = "{0:>4}{1:>6}{2:>7}{3:>8}{4:>14}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))


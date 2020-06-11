import math
from functools import reduce
d= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

a= lambda x:x+3
print(a(5))

b= lambda x:2*x
print(list(map(b,d)))

c = lambda x: x%2 == 0 
print(list(filter(c,d)))

#Find primes 1-100 without using loops.

d = range(4,1001)
r = list(map(lambda c: math.floor(math.sqrt(c)),d))
print(r)

for n in range(2,1001):
    if(n-2<2):
        print(n)

    else:
        rem = list(map(lambda x: n%x, range(2,r[n-4]+1)))
        #b = reduce(lambda a,b: a if (a < b) else b, rem)
        if 0 not in rem:
            print(n)

 

from utility import *
import math

N = 50512
M=10000000
c=0
primes = getPrimes(M)
while N<M:
    f = getPrimeDivisors(N)
    if len(f) == 4:
        c=c+1
        if c>=2:
            print N, f, c
    else:
        c=0

    if c== 4:
        print "!!!!", N-3
        break
    N=N+1

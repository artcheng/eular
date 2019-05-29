from utility import *
import decimal

def sums( N ):
                x = [N-1, 1]
		while x[0]>=x[1]:
			yield x
			x[0] = x[0]-1
			x[1] = x[1]+1

		last = 1
		while True:
                	for sl in sums(N-last):
				x=sl+[last]
				yield x
			last = last +1
					

N=10
p=decimal.Decimal(0.0)+N*N*math.factorial(N-1)
FACN = math.factorial(N)

for g in sums(N):
	c=lcmmm(g)
        leftN = N
        total=1
        counter={}
        for n in g:
                if n not in counter:
                        counter[n] = 0
                counter[n] = counter[n]+1
                m=math.factorial(n-1)

                nn = nCr(leftN, n)*m
                total = total * nn
                leftN = leftN -n

        x = total
        for k in counter.keys():
                x=x/math.factorial(counter[k])

        csqr = c*c
        p = p + x*csqr

        print g, ":", x,"X", csqr, p/FACN
        if g[0]== 1:
                break
        #print g[0], p/FACN
print p/FACN

	


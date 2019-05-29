from utility import *

def sums( N ):
        yield [N]
        for n in range (1, N):
               for sl in sums(n):
                       if sl[0]<=N-n:
                                yield [N-n]+sl

N=20
p=0.0
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

	#print g, x, csqr
	if g[0]== 1:
		break

print p/math.factorial(N)
	
		
	

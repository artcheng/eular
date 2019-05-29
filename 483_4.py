from utility import *
import decimal

def sums( N ):
		yield [N]
		yield [N-1, 1]
        	for n in range (2, N):
              		for sl in sums(n):
                      		if sl[0]<=N-n:
                             		yield [N-n]+sl

N=3
p=decimal.Decimal(0.0)
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

	print g, ":", x,"X", csqr
	if g[0]== 1:
		break
	#print g[0], p/FACN
print p/FACN
	
		
	

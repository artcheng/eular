from utility import *

M=10000
primes =getPrimes(M)


n=M/2
while True:
	v = (n+1)*n/2

	x=1
	for p in primes:
		if p>n:
			break
		c=1
		if v%p==0:
			pf = p
			while v%pf ==0:
				c = c+1
				pf = pf*p
		x=x*c

	print n, v, x
	if x>500:
		break
	n=n+1
		




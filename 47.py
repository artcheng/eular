from utility import *
import math

n=90

c=0
M = 1000000
primes = getPrimes(M)

C=4
print 'starting-----'
while n<M:
	dc = 0
	for p in primes:
		if p > math.sqrt(n+1):
			break
		if n%p == 0:
			dc = dc+1
		if dc>C:
			break
	if dc == C:
		c = c +1
	else:
		c = 0

	if c==C:
		print n, dc
		break

	n = n+1
			

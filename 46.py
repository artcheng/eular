from utility import *

M=10000
primes =getPrimes(M)

ps = {}
for p in primes:
	ps[p] = 1

i=33

while i< M:
	i = i+1
	if i in ps:
		continue

	if i%2 == 0:
		continue

	for p in primes:
		s = (i-p)/2
		if s< 0:
			print '----', i
			break
			

		if isSquare(s):
			break
	

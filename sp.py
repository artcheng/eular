from utility import *
from collections import OrderedDict

M=50

counter={}
primes= getPrimes(M)

for i in primes:
	for j in primes:
		counter[i+j] = -100000

for i in range (2,100):
	for j in range(2, 100):
		if i==j:
			continue
		s=i+j
		if s==17:
			print i, j
		if s>100:
			continue
		counter[s] = counter.get(s,0)+1


for sum in counter:
	if counter[sum]>0:
		print sum, counter[sum]/2

from utility import *

M=1000000

allP = getPrimes(M)

allPM={}
count = 0
for d in allP:
	allPM[d] = True
	count = count+1

for d in allP:
	b = 10
	while b<d:
		r = d%b
		c = str(r) + str( (d-r)/b )
		if int(c) not in allPM:
			#allPM[c] = False
			count = count-1
			break		
		b = b*10 


print count




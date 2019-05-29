from utility import *
ps= getPrimes(1000000)

allP={}
for p in ps:
	allP[p] = 0

count = 0
sum = 0
for p in ps:	
	if p< 10:
		continue
	s = str(p)
	l = len(s)
	check = True
	for i in range(1, l):
		n = int( s[i:])
		if n not in allP:
			check = False
			break
		m = int( s[0: l-i])
		if m not in allP:
			check = False
			break


	if check:
		count = count+1
		sum = sum + p
		print count, p


print sum


from utility import *
from decimal import *
getcontext().prec = 1000

ps= getPrimes(1000)

one = Decimal(1.0)

x=0
n=0

for i in range(3, len(ps)):
	p = Decimal(ps[i])

	d = Decimal(one/p) 
	s=str(d)[2:]
	#print s

	for i in range(1, len(s)):
		ss=s[:i]
		ds = Decimal(int(ss))

		sds = str(ds*p)
		done = True
		for c in sds:
			if c!='9':
				done = False
				break
		if done:
			if ds>x:
				x=ds
				n=p
			#print ds, ds*p
			if p-i==1:
				print p, i, p%9
			break
	


print n	

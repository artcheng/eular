from utility import *
import time

st=time.time()
N=100

d1={1: 1.0}
d2={1: 0.5, 2: 0.5 }
listD=[d1, d2]

for n in range(3, N+1):
	dk = {n: 1.0/n}
	for k in range (1, n):
		for p, w in listD[n-k-1].iteritems():
			newp = max(k, p)
			if newp in dk:
				dk[newp] = dk[newp]+w/n
			else:
				dk[newp] = w/n
	listD.append(dk)
	#print listD


for n in range(1, N):
	a = 0
	numa = 0
	for p, w in listD[n].iteritems():
		if p<= (N/2):
			a = a+1*w
		numa = numa+1
	
	print n+1, numa, a	

#print time.time()-st


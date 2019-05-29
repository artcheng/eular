from utility import *
import numpy
import datetime

N=200

LUM = []

for i in range(0, N+1):
	LUM.append({})

def f(n, k):
	if k in LUM[n]:
		return LUM[n][k]
	else:
		if n<=1:
			return 1.0*k*k
		else:
			x=0.0
			for m in range(0, n):
				x=x + f(m, lcm(n-m, k))

			LUM[n][k]=x/n

		return LUM[n][k]

starttime=datetime.datetime.now()
print starttime
v=f(N, 1)
print v

endtime=datetime.datetime.now()
print endtime
print 'duration: {0}'.format(endtime-starttime)

#print LUM

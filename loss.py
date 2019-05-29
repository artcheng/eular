from utility import *


M=4
print "n! = ",math.factorial(M)
p=0.0
All = reGroup(M)
for gk in All.keys():
	g = All[gk]

	if min(g)==1:
		continue

	leftM = M
	total=1
	counter={} 
	for n in g:
		if n not in counter:
			counter[n] = 0
		counter[n]=counter[n]+1
		m=math.factorial(n-1)

		nn = nCr(leftM, n)*m
		total = total * nn
		leftM = leftM-n
	x = total
	for k in counter.keys():
		x = x / math.factorial(counter[k])

	p = p + x

	print g, x
print "all wrong cases:", p
print "probability:", p/math.factorial(M)
	
			

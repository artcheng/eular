from utility import *


#M = 350
M=4
print math.factorial(M)
p=0.0
All = reGroup(M)
print M, len(All)
#vcter={}
for gk in All.keys():
	g = All[gk]
	c=lcmmm(g)
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

	csqr = c*c
	p = p + x*csqr

	#if csqr not in vcter:
	#	vcter[csqr]=x
	#vcter[csqr] = vcter[csqr]+x

	print g, csqr, x
#print vcter
print p
print p/math.factorial(M)
	
			

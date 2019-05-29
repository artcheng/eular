from utility import *
import math

allPrime = getPrimes(100)

twoF = {}
for a in allPrime:
	for b in allPrime:
		#print a+b, a, b
		twoF[a+b] = 1

noTwoF={}
for i in range(4, 100):
	if i not in twoF:
		print i
		noTwoF[i]=0


ppp={}
for p in range(4, 250):
	counter = 0
	for a in range(2,p):
		if p%a == 0:
			b = p/a
			s = a+b
			if s in noTwoF:
				#print p, a, b, s, counter
				counter= counter+1
				ppp[p]=ppp.get(p, 0)+1
		 


print "-------------"
	
ccc={}
for p in ppp:
	if ppp[p]==2:
		for a in range(2,p):
                	if p%a == 0:
                        	b = p/a
                        	s = a+b
				if s in noTwoF:
					print p,a,b,s
					ccc[s] = ccc.get(s,0)+1


print ccc

for c in ccc:
	if ccc[c] == 2:
		print c

from utility import *

d=[0,1,2,3,4,5,6,7,8,9]

for p in permutations(d, 2):
	num = p[0]*10+p[1]
	for pp in permutations(d, 2):
		den = pp[0]*10+pp[1]
		if num>den:
			continue
		
		if p[0]==pp[1] :
			n1 = p[1]
			n2 = pp[0]
		elif p[1]==pp[0]:
			n1 = p[0]
			n2 = pp[1]
		else:
			continue

		if n2==0 :
			continue

		d1 = 1.0*num/den
		d2 = 1.0*n1/n2

		if d1==d2:
			print num, den


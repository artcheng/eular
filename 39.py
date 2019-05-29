import math
from utility import *

ct = {}
for c in range(2, 1000):
	for a in range (1, c):
		b_sqr = (c+a)*(c-a)
		if isSquare(b_sqr):
			b = math.sqrt(b_sqr)
			if b>=c:
				continue
			print a, b, c
			cc = a+b+c
			if cc < 1000:
				ct[cc] = ct.get(cc, 0) +1


m = 0
cc = 0
for c in ct:
	if ct[c] > m:
		m = ct[c]
		cc = c


print cc, m	

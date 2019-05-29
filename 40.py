import math

N = 1

p = 0

i = 0

while p<= 1000000 :
	s = str(N)
	p = p + len(s)

	pp =  math.pow(10, i)
	if p >= pp:
		i = i + 1
		d = int(p-pp)
		print p, N, d, s[len(s)-d-1]

	N = N + 1 

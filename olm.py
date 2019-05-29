from utility import *


N=11

t={}
for n in range(1, N+1):
	M = math.factorial(n)
	x = 0
	print n, M, len(getDivisors(M))+1, n*(n+1)/2

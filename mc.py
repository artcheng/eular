from utility import *

def game(N,M,d):
	for di in d:
                if N<0:
                        return N,M,"---", N%M, "bad"
                elif N%di == 0:
                        return "good"
                else:
                        N = N-di
        return N,M,"===",N%M,"bad"

Ps=getPrimes(10)


for p in Ps:
	M=2**(p-1)*p
	d=[]
	for i in range(1, 15):
		d.append(2**i)
		d.append(2**(i-1)*p)

	print M, d


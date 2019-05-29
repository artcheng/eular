from utility import *

for n in range(10, 90000):
	s = str(n)
	fs = 0
	for c in s:
		fs = fs + math.factorial(int(c))
		if fs>n:
			break

	if fs==n :
		print n, fs


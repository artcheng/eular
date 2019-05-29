from utility import *
import math

M = 4
x = 0.0
for p in all_perms(range(0,M)):
 	temp = list(p)	
	y=circleDecomp(p)
	print temp, y

	if y<= 5 :
		x=x+1

print x, math.factorial(M), x/math.factorial(M)


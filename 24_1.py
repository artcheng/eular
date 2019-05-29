<<<<<<< HEAD
import math

fac=[]

for i in range (0,10):
	fac.append(math.factorial(i))

d=[0,1,2,3,4,5,6,7,8,9]
v=[0,1,2,3,4,5,6,7,8,9]

w=999999

for i in range(0, 10):
	j = 9-i
	x = w/fac[j]
	v[i] = d.pop(x)
	print v
	w = w%fac[j]
		
	
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 23:10:16 2015

@author: art
"""
import math

f=[]
for i in range(1,10):
    f.append(math.factorial(i))
    
print f
x=1

v=[0,0,0,0,0,0,0,0,0,0]

j=9

while x>0:
    print f[j-1]
    if x>=f[j-1]:        
        x=x-f[j-1]
        print x
        v[10-j]=v[10-j]+1
        print j
        print v
    else:
        print "-",j
        j = j-1
        
        
>>>>>>> origin/master

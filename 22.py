# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:23:15 2015

@author: art
"""

f=open("p022_names.txt", 'r')

for line in f:
    n=line.strip().split(",")

for i in range(0, len(n)):
    n[i] = n[i][1:-1]
n= sorted(n)

x=0

for i in range(0, len(n)):
    nn = n[i]
    w=0
    for c in nn:
        w=w+ord(c)-64
    print i+1, w    
    x = x+w*(i+1)
    
    
print x   
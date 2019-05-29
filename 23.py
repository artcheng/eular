# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:37:31 2015

@author: art
"""

from utility import *

M=20813

d=[]
for n in range(1, M+1):
    divs = getDivisors(n)
    s = sum(divs)
    #print n, s
    if s>n:
        d.append(n)

k={}
l = len(d)
for i in range (0,l):
    for j in range(0, l-i):
        #print d[i], d[(i+j)%l]
        k[d[i]+d[(i+j)%l]] = 1
        
x=0
for i in range(1, M):
    if i not in k:
        x=x+i

print x        
 




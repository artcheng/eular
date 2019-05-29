# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:01:52 2015

@author: art
"""

from utility import *

M=10000
d={}
for n in range(1, M+1):
    divs = getDivisors(n)
    d[n]=sum(divs)
    
x=0

for a in d.keys():
    b = d[a]
    if b<M and a!=b:
        if d[b]==a:
            print a, b
            x=x+a
            
print x            
        
        
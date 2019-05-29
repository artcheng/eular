# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 00:05:01 2015

@author: art
"""

ps=[2,3,5,7,11,13]

i=6

a=14

while i<10001:
    a=a+1
    isp = True
    for p in ps:
        if a%p==0:
            isp = False
            break
    if isp:
        ps.append(a)
        i=i+1
        print i, a
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def palindrome(num):
    return str(num) == str(num)[::-1]

i=999


while i>900:
    j=999    
    while j>=i:
            x=i*j
            if palindrome(x):
                print x
            j=j-1
    i=i-1    
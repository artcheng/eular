from utility import *
import time


def cal2(inp):
    st_time=time.time()
    ank=[{1:0.0} for x in range(0,inp+1)]
    for n in range(inp,1,-1):
        for m in range(2,n):
            for k,v in ank[n].iteritems():
                k1=lcm(n-m,k)
                ank[m][k1]=0.0
    
    for n in range(2,inp+1):
        for k,v in ank[n].iteritems():
            a=lcm(n,k)
            b=lcm(n-1,k)
            a=a*a+b*b
            for m in range(2,n):
                k1=lcm(n-m,k)
                b=ank[m].get(k1,0)
                a=a+b
            ank[n][k]=a*1.0/n
    print n, len(ank[2]), ank[n][1], time.time()-st_time

N=4
cal2(N)

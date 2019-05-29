import math
import datetime
import sys
import array

total = int(sys.argv[1])
fac_cache=[0]*(total+1)

# cache indexed by m first, then n, both from small to large
permcount_cache=[0]*(total/2)
for i in range(total/2):
    permcount_cache[i]=[0]*(total-1-i)
lcm_cache=[0]*(total/2)
for i in range(total/2):
    lcm_cache[i]=[0]*(total-1-i)

fratios_cache=[0]*total  #just for total!/n!

def my_factorial(n, cache):
    if n==1: return 1
    if cache[n]==0:
        cache[n]=n*my_factorial(n-1,cache)
    return cache[n]

def fratio(j):
    if j==total: return 1
    if fratios_cache[j-1]==0:
        fratios_cache[j-1]=my_factorial(total,fac_cache)/my_factorial(j,fac_cache)
    return fratios_cache[j-1]

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    if a%b==0: return a
    return a//gcd(a, b)*b

def merge_dl(list_1, list_2, dl_entries):
    done=False
    for k in range(len(list_2)):
        if list_2[k]==dl_entries[1]:
            list_1[k]=list_1[k]+dl_entries[0]
            done=True
    if not done:
        list_2.append(dl_entries[1])
        list_1.append(dl_entries[0])

# given integers n and m, return the list of partition perm counts
# and lcms for each partition of n elements containing cycles with max length
# equal to m, assuming m<=n
# the count is sum of total!/a1!a2!...aN!*1^a1...N^aN for
# all a1,...,aN corresponding to a given lcm value
def perm_counts_and_lcms(n, m):
    if m==1:
        return [fratio(n)], [1]
    if m<total/2:
        lcm_from_cache=lcm_cache[m-2][n-m]
        if lcm_from_cache != 0:
            #if m>=total/2: print 'use cache {0},{1}'.format(n,m)
            return permcount_cache[m-2][n-m], lcm_from_cache
    aList1 = []
    aList2 = []
    i=1
    while m*i<=n:
        if m*i==n:
            merge_dl(aList1, aList2, [fratio(i)/m**i,m])
        else:
            multiplier=my_factorial(i,fac_cache)*m**i
            for j in range(1, min(m,n-m*i+1)):
                permcounts,lcms=perm_counts_and_lcms(n-m*i,j)
                for k,aLcm in enumerate(lcms):
                    newLcm=lcm(aLcm,m)
                    newCount=permcounts[k]/multiplier
                    merge_dl(aList1, aList2, [newCount,newLcm])
        i=i+1
    if m<total/2:  #otherwise never got reused
        permcount_cache[m-2][n-m]=aList1
        lcm_cache[m-2][n-m]=aList2
    return aList1,aList2

starttime=datetime.datetime.now()
print starttime

total_sum = 0
total_perm_count=0
for i in range(total, 0, -1):
    permcount_list,lcm_list=perm_counts_and_lcms(total,i)
    
    print i, permcount_list, lcm_list
    if i>1:
        if i<total/2:   # cache for m=i will never be needed again
            del permcount_cache[-1]
            del lcm_cache[-1]

    for j,pc in enumerate(permcount_list):
        total_perm_count=total_perm_count+pc
        total_sum=total_sum+pc*lcm_list[j]**2

print total_sum
print total_perm_count
print '%.10f' % (total_sum*1.0/total_perm_count)
endtime=datetime.datetime.now()
print endtime
print 'duration: {0}'.format(endtime-starttime)

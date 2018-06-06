M=2000000
N = range(0, M+1) 


n=2
sum=0
while n<M:
	if N[n] != 0:
		sum=sum+n
		j = 2*n
		while j<M+1:
			N[j]=0
			j=j+n
	n=n+1


print sum

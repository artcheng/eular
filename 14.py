
def chain(N):

	s=N
	i=0
	while s!=1 :
		i = i+1
		if s%2==0:
			s = s/2
		else:
			s=3*s+1
	return i+1



n=1000000

x=0
while n>0:
	xx=chain(n)
	if xx>x:
		x=xx
		print n, xx	

	n=n-1



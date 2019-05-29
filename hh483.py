from utility import *
import decimal

N = 3

prime=[False]
primepow=[0]

for i in range(1, N+1):
	prime.append(True)
	primepow.append(1)

prime[1] = False;

for i in range(1, N+1):
	if prime[i]:
		j=i
		while j<=N :
			primepow[j]=i
			j = j*i

		print primepow
		for j in range(i+i, N+1, i):
			prime[j]=False

print primepow
print prime

dp={}
dp[(0.0,1.0)]=1.0

for v in range(N, 0, -1):
	print ""
	print v
	ndp={}
	for k in dp.keys():
		print k, dp[k]
		s = k[0]
		g = k[1]
		num = dp[k]

		gv = g

		if g%v==0 :
			gv = g/primepow[v]

		state=(s, gv)
		if state in ndp:
			ndp[state] = ndp[state]+num
		else:
			ndp[state]=num

		print "-->",state, ndp[state]

		print "-*-",ndp

		m= v/gcd(g, v)
		g = g*m
		g = g/primepow[v]


		num = num*m*m

		c=1
		while v+s <= N:
			s = s+v
			num = num/v
			num = num/c

			state = (s, g);
			if state in ndp:
				ndp[state] = ndp[state]+num
                	else:
                        	ndp[state]=num
				
			print "---->",state, ndp[state]
			#print "------", ndp
			c = c+1

		state = (s, g)
	dp = ndp
	print "-", dp

res = 0.0
for k in dp.keys():
	print k, dp[k]
	if k[0] == N:
		res = res +dp[k]

print res

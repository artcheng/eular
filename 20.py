x=1

for i in range(1, 100):
	if i%10 == 0:
		x=x*i/10
	else:
		x = x*i

xs = str(x)

s=0
for c in xs:
	s=s+int(c)

print s	

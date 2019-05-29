import math
S=20
P=6
T = S+P

tenF = math.factorial(10)


def addOneMorePlus(ca):
	newCases={}

	for c in ca.keys():
		for i in range(0,T):
			lc=list(c)
			if c[i]=="!":
				lc[i]="+"
				newCases["".join(lc)]=True

	return newCases

start=""
for i in range(0,T):
	start=start+"!"
		
cases={start: True}
for p in range(0, P):
	cases = addOneMorePlus(cases)

color=0.0
casetotal=0.0

for c in cases.keys():
	ca = c.split("+")
	i = 0
	p = 1
	valid = True
	for g in ca:
		k = len(g)
		if k>10:
			valid=False
			break	
		elif k>0:
			i=i+1
			p=p*tenF/math.factorial(k)/math.factorial(10-k)

	if valid:
		color=color+i*p
		casetotal = casetotal +p


print len(cases.keys())
print color/casetotal
	

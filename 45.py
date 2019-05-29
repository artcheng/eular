
i = 2
allT = {}
allP = {}
allH = {}

def getTNum( n ):
	global allT
	global allP
	global allH

        if n not in allT:
                v =  n*(n+1)/2
                allT[n] = v
		vp = n*(3*n-1)/2
		allP[vp] = n
		vh = n*(2*n-1)
		allH[vh] = n

        return allT[n]

i=1
while True:
	vT = getTNum(i)
	#print i, vT
	if vT in allP and vT in allH:
		print "------", i, vT
	i = i + 1

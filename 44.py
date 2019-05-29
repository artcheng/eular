
i = 2
allP = {}
pDic = {}
allP[1] = 1
pDic[1] = 1

maxN = 0

def getPNum( n ):
	global allP
	global pDic
	global maxN

        if n not in allP:
                v =  n*(3*n-1)/2
                allP[n] = v
                pDic[v] = n
	if n>maxN:
		maxN=n
		#print maxN, v

        return allP[n]

def addPupto( p ):
	global maxN
	m = maxN
	while getPNum(m) <=p:
		m = m + 1

	#print maxN

while i<10000:
	for j in range( 1, i):
		#print i, j
		sum = getPNum(i) + getPNum(j)
		addPupto(sum)
		#print diff
		if sum in pDic:
			#print i, j, pDic[sum], sum
			diff = getPNum(i) - getPNum(j)
			if diff in pDic:
				print "-----", i, j, pDic[diff], diff

 

	i = i + 1

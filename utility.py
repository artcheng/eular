import math

def isSquare( N ):
	if N== 1:
		return True
	x = N // 2
	seen = set([x])
	while x * x != N:
		x = (x+(N // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True	

def getPrimes(M):
	N = range(0, M+1) 


	n=2
	while n<M:
		if N[n] != 0:
			j = 2*n
			while j<M+1:
				N[j]=0
				j=j+n
		n=n+1

	result=[]
	N.pop(1)
	for n in N:
		if n!=0:
			result.append(n)
	return result

def getReversDivisors(M):
	nums=[]
	for n in range(M, 0, -1):
		nums.append(n)


	result=[]
	ps=getPrimes(M)
        for p in reversed(ps) :
                for i in range(0, M):
                       if nums[i]>0 and nums[i]%p == 0:
				result.append(nums[i]) 
				nums[i]=0
        
	result.append(1)
	return result

 
 
def getDivisors(M):
	result=[1]
	for i in range(2, M/2+1):
		if M%i == 0:
			result.append(i)
                 
	return result

def getPrimeDivisors(M):
	result=[]
	primes = getPrimes(M)
	for p in primes:
		if M%p == 0:
			result.append(p)
	return result

def getPrimeDivisors2(M, primes):
        result=[]
        for p in primes:
                if p>M:
                    return result
                if M%p == 0:
                        result.append(p)
        return result


def eular(M):
	result=M
	p = getPrimes(M)
	for pp in p:
		if M%pp==0:
			result = result*(pp-1)/pp

	return result
        
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def circleDecomp( perm ):
	ci = 0
	cc = []
	#allCircle = []
	i = 0
	maxL = 1
	allL = {1:True}
	while i<len(perm):
		if perm[ci] ==-2:
			#allCircle.append(cc)
			if len(cc) not in allL:
				allL[len(cc)] = True
				maxL = lcm(maxL, len(cc))
			cc=[]
			i=i+1
			ci=i
		elif perm[ci]==-1:
			i=i+1
			ci=i
		else:
			cc.append(ci)
			oldci = perm[ci]
			if len(cc)==1:
				perm[ci]=-2
			else:
				perm[ci]=-1
			ci = oldci
	#print allCircle, maxL

	return maxL

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def lcmmm( nums ):
	r = 1
	for n in nums:
		if n!=1:
			r=lcm(r, n)
	return r

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def listToStr(L):
	x = ""
	for l in L:
		x=x+str(l)
	return int(x) 

def reGroup(N):
	if N==1:
		return {"1":[1]}
	else:
		result={}
		rN_1 = reGroup(N-1)
		for r in rN_1.keys():
			newr = list(rN_1[r])
			newr.append(1)
			newr = sorted(newr)
			result[listToStr(newr)]=newr
		for rk in rN_1.keys():
			ct={}
			r = rN_1[rk]
			for i in range(0, len(r)):
				if r[i] not in ct:
					ct[r[i]]=1
					nr = list(r)
					nr[i] = nr[i]+1
					nr = sorted(nr)
					result[listToStr(nr)] = nr
		return result

def findPrimitiveRoot(N, a, tested):

	for d in range(2, N):
		a=d
		if N%a != 0 and a not in tested:
			print ">>>> chose a: ", a
			break 

	
	t=a%N
	for i in range(1, N):
		print i, t
		if t!= 1:
			tested.append(t)
			t=(t*a)%N
		else:
			if i==N-1:
				print a, "is p-root"
				return a
			else:
				for d in range(2, N):
					if d not in tested:
						return findPrimitiveRoot(N, d, tested)

def digitSum(x):
	str_x =str(x)
	t=0
	for c in str_x:
		t += int(c)
	return t
		
	

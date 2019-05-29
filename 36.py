def isPalindromic( n ):
	s = str( n )
    	l = len(s)
	for i in range(0, l):
		if s[i] != s[l-1-i]:
			return False

	s = bin(n)[2:]
	l = len(s)
        for i in range(0, l):
                if s[i] != s[l-1-i]:
                        return False

	return True

N = 1000000

sum = 0
for i in range (0, N):
	if isPalindromic( i ):
		print i, bin(i)
		sum = sum + i

print sum

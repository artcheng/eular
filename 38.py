def checkPand(n):
	if n< 100000000 or n>987654321 :
		return False

	else:
		digs = {}
		s = str(n)
		for c in s:
			if c == '0':
				return False
			if c in digs:
				return False
			else:
				digs[c] = 1

		return True


n = 1
lim = 987654321/50
while n<lim:
	sum = n
	m = 2
	while sum < 987654321:
		s = str(sum)+str(n*m)
		sum = int(s)
		if checkPand(sum):
			print n, m, sum
			break
		m = m+1
	n = n+1

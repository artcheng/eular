s = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
t = [3, 6, 7, 8, 7, 7, 7, 9, 8, 8]
tt= [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

ss = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
st = ["ten", "eleven", "tweleve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
stt = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

	
def writenumber(n):
	if n < 10:
		print ss[n]
		return s[n]
	elif n < 20:
		print st[n-10]
		return t[n-10]
	elif n < 100:
		a = n/10
		b = n%10
		print stt[a], ss[b]
		return tt[a] + s[b]
	elif n < 1000:
		a = n/100
		b = n%100
		x = 0
		print ss[a]+" hundred"
		x = s[a]+7

		if b>0:
			print " and "
			x = x+3
			x=x+writenumber(b)

		return x
	else:
		print "one thousand"
		return 11
		
		
		
x=0
for i in range (1, 1001):
	print "----------", i
	y = writenumber(i)
	print y
	x=x+y

print x

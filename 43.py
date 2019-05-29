from utility import *

ps = getPrimes(20)

nums = all_perms(range(0,10))

sum=0
for na in nums:
	if na[0] == 0:
		continue
        sn = ''.join(str(e) for e in na)
        n = int(sn)

	b = True

	for i in range(1, 8):
		sa = sn[i: i+3]
		a = int(sa)
		if a% ps[i-1] != 0:
			b = False
			break	 
	if b :
		print n
		sum = sum + n


print sum

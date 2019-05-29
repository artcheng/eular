from utility import *

ps = getPrimes(99997)

nums = all_perms(range(1,8))
max=0
for na in nums:
	sn = ''.join(str(e) for e in na)
	n = int(sn)
	b = True
	for p in ps:
		if n%p == 0:
			b = False
			break

	if b :
		if n>max:
			max = n
			print max


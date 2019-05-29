import math
import decimal

f=decimal.Decimal((1+math.sqrt(5))/2)
k=decimal.Decimal((1-math.sqrt(5))/2)
f=math.log(f, 10)
d=decimal.Decimal(math.sqrt(5))


n=400

while True:
	F=f*n - math.log(d)
	if F>=998.5:
		print n, F
		break

	n=n+1

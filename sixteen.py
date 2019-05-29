from decimal import *

x=Decimal(2**15)

sx = str(x)

y=0
for c in sx:
	y = y+int(c)	

print y

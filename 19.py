year = 1900

M=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d=0
w=1
x=0
while year<2001:
	#print year
	if (year%100 != 0 and year%4==0) or (year%400==0):
		M[1]=29
	else:
		M[1]=28

	i=0
	for m in M:
		if w==6 and year>1900:
			x=x+1
		d=d+m
		w = d%7
		#print d, m, w
		
			

	year = year+1


print x
		
		
		
		 

def my_range(start, end, step):
	while start <= end:
        	yield start
        	start += step

for c in range (300, 1000):
	x=(1000.0 - c)/2
	csq = 1.0*c*c
	for y in my_range(1, x, 0.5):
		if 2.0*x*x + 2.0*y*y == csq:
			print x+y, x-y, c, (x+y)*(x-y)*c


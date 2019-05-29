import math

f = open('words42.txt', 'r')

contents = f.read()
words = contents.split(",")

count = 0
for wd in words:
	if wd == "" :
		continue

	w = wd[1:-1]
	s = 0
	for c in w:
		s = s + ord(c)-64

	x = s * 2
	a = math.floor(math.sqrt(x))
	y = a*(a+1)

	if y == x: 
		count = count +1
		print w, s, a, a*(a+1)/2

print count

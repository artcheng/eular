f = open("thirteen.txt", 'r')

d=[]
x=0
for line in f:
	d.append(int(line.strip()[:11]))

for n in d:
	x = x+n
print x

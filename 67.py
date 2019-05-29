f = open("sixtyseven.txt", 'r')

d=[]
x=0
for line in f:
	d.append(map(int,line.strip().split(" ")))


l=len(d)
for i in range(1, l):

	for j in range(0, i+1):
		if j==0:
			d[i][j]=d[i][j]+d[i-1][j]
		elif j==i:
			d[i][j]=d[i][j]+d[i-1][j-1]
		else:
			d[i][j]=d[i][j]+max(d[i-1][j], d[i-1][j-1])


		
		

print max(d[l-1])

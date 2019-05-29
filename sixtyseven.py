f = open("sixtyseven.txt", 'r')

d=[]
x=0
for line in f:
	d.append(map(int,line.strip().split(" ")))


for i in range(0, 20):
	for j in range (0, 20):
		if j<16:
			s1 = d[i][j]*d[i][j+1]*d[i][j+2]*d[i][j+3]
			if s1>x:
				x=s1

		if i<16:
			s2 = d[i][j]*d[i+1][j]*d[i+2][j]*d[i+3][j]
			if s2>x:
				x=s2

		if i<16 and j<16:
			s3 = d[i][j]*d[i+1][j+1]*d[i+2][j+2]*d[i+3][j+3]
			if s3>x:
				x=s3

			s4 = d[i+3][j]*d[i+2][j+1]*d[i+1][j+2]*d[i][j+3]
			if s4>x:
                                x=s4


		
		


print x

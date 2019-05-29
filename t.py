from utility import *
from collections import OrderedDict


D = [[1,2], [2,3],[2,4],[2,5],[2,6],[1,3],[1,4],[1,5],[1,6],[3,4],[3,5],[3,6],[4,5],[4,6],[5,6]]

P=[]

def gV (i, j):
	return D[P[i]][j]

i=1
for p in all_perms(range(0,len(D))):
	print i
	i = i+1
	P = p
	if gV(0, 0)+gV(0, 1) + gV(1, 0) + gV(2, 0) + gV(3, 0) + gV(3, 1) != 23:
		continue
	if gV(4, 1)+gV(5, 1) + gV(6, 0) + gV(6, 1) + gV(7, 1) + gV(8, 1) != 29:
                continue 
	if gV(9, 1)+gV(13, 0) + gV(13, 1) + gV(14, 0) + gV(14, 1) + gV(12, 1) != 16:
                continue
	if gV(0, 0)+gV(4, 0) + gV(4, 1) + gV(9, 0) + gV(9, 1) != 16:
                continue
	if gV(0, 1)+gV(5, 0) + gV(5, 1) + gV(10, 0) + gV(13, 0) != 27	:
                continue
	if gV(2, 0)+gV(2, 1) + gV(6, 1) + gV(11, 0) + gV(14, 0) != 15:
                continue
	if gV(3, 0)+gV(7, 0) + gV(7, 1) + gV(11, 1) + gV(14, 1) != 27:
                continue

	for q in P:
		print D[q]
		break

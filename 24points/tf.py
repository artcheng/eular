totalCal = 0
solSet = []

def group(arry):
	result = []
	for i in range(1, pow(2,len(arry)-1)):
		s = str(bin(i))[2:]
		while len(s)<len(arry):
			s="0"+s
		group1=[]
		group2=[]
		for j in range(0, len(s)):
			if s[j]=='0':
				group1.append(arry[j])
			else:
				group2.append(arry[j])

		result.append([group1, group2])
	return result

def allV(arry):
	global totalCal
	global N

	result = {}
	if len(arry)==1:
                result = {}
		result [arry[0]] = str(arry[0])
	else:
		groups = group(arry)
		for g in groups:
			V_g0 = allV(g[0])
			V_g1 = allV(g[1])

			for v in V_g0:
				for w in V_g1:
					result[v+w]="("+V_g0[v]+"+"+V_g1[w]+")"
					s = "("+V_g0[v]+"-"+V_g1[w]+")"
					if v==w:
						result[0.0]= s
					else:
						result[v-w]= s
						result[w-v]= "("+V_g1[w]+"-"+V_g0[v]+")"
						totalCal = totalCal+2
					result[v*w]= "("+V_g0[v]+"*"+V_g1[w]+")"
					totalCal = totalCal+2	
					if w!= 0.0:
						result[v/w]="("+V_g0[v]+"/"+V_g1[w]+")"
						totalCal = totalCal+1
					if v!= 0.0:
						result[w/v]="("+V_g1[w]+"/"+V_g0[v]+")"
						totalCal = totalCal+1
					if len(arry)==N and result.get(24.0, "") != "":
						print result.get(24.0), "  total calculation:", totalCal
						quit()
	return result


input = [3.0, 12.0, 12.0, 12.0];
N = len(input)
cal = allV(input)
print cal

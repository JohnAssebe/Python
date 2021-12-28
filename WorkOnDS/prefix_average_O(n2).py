def prefix_avg(s):
	n=len(s)
	A=[0]*n
	for i in range(n):
		total=0
		for k in range(i+1):
			total+=s[k]
		A[i]=total/(k+1)
	yield A
for k in prefix_avg([1,2,3,4,5]):
	print(k)
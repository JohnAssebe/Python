def prefix_avg(s):
	n=len(s)
	lst=[0]*n
	
	total=0
	for i in range(n):
		total+=s[i]
		lst[i]=total/(i+1)
	yield lst
for k in prefix_avg([1,2,3,4,5]):
	print(k)

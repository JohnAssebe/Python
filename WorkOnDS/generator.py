# Generators use yield instead of return 
def factors(n):
	for i in range(1,n+1):
		if n%i==0:
			yield str(i)+" -> "+str(n)+' / '+str(i)+ " = " +str(n//i)
# print(type(factors(120))) # returns  <class 'generator'> 
# print(factors(120)) # returns <generator object factors at 0x039CC5D8>
for i in factors(120):
	print(i)



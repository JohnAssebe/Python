num = int(input())
def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
if num<0:
    print("Error")
else:
    for i in range(num):
        print(fibonacci(i))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for _ in range(n):
    expression=input()
    sol=True
    try:
        re.compile(expression)
    except:
        sol=False
    print(sol)

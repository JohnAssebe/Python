import sys
from functools import reduce
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int,input().strip().split(' '))
B = map(int,input().strip().split(' '))
def gcd(c,d):
    while c%d!=0:
        c,d=d,c%d
    return d
def LCM(a, b):
    return (a*b)//gcd(a,b)

lcm = reduce(LCM, A, 1)
gcd = reduce(gcd, B)

lcm_copy = lcm

count = 0
while lcm <= gcd:
    if(gcd % lcm) == 0:
        count += 1
    lcm = lcm + lcm_copy

print(count)

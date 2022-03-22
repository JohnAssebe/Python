#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a=sorted(a)
    max_=0
    for i,item in enumerate(a):
        if i < len(a)-1:
            if a[i]==a[i+1]:
                if max_< a.count(a[i]):
                    max_=a.count(a[i])
            elif(a[i+1]-a[i]<=1):
                if max_ < a.count(a[i])+a.count(a[i+1]):
                    max_=a.count(a[i])+a.count(a[i+1])
    return max_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

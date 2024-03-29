#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
def diagonalDifference(arr):
    left_to_right=0
    right_to_left=0
    for i in range(len(arr)):
        left_to_right+=arr[i][i]
    for i in range(len(arr)):
        right_to_left+=arr[i][len(arr)-1-i]
    return abs(left_to_right-right_to_left)
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

def pageCount(n, p):
    min_page=p//2
    if n==p+1 and n%2==0 and n>2:
        return 1
    if min_page>(n-p)//2:
        min_page=(n-p)//2
    return min_page

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

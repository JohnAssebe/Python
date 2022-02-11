#!/bin/python3

import math
import os
import random
import re
import sys
def migratoryBirds(arr):
    set_arr=set(arr)
    max_=arr[0]
    for sight in set_arr:
        if arr.count(sight)>arr.count(max_):
            max_=sight
        else:
            arr.remove(sight)
    return max_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

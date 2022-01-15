#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
        counter=Counter(s).values()
        mod_remain=0
        for i in counter:
            mod_remain+=i%2
        return "NO" if mod_remain>1 else "YES" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

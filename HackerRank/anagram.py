#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def anagram(s):
    if len(s)%2: return -1
    else:
        half=len(s)//2
        string1=s[0:half]
        string2=s[half:]
        counterstr1=Counter(string1)
        counterstr2=Counter(string2)
        return half - sum((counterstr1&counterstr2).values())
if __name__=="__main__":
    for _ in range(int(input())):
        print(anagram(input()))     

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         s = input()

#         result = anagram(s)

#         fptr.write(str(result) + '\n')

#     fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
 

def dayOfProgrammer(year):
    if(year<1918):
        if(year%4==0):
            day=12
        else:
            day=13
    elif(year==1918):
        day=26
    else:
        if (year%4==0 and year%100!=0 ) or year%400==0:
            day=12
        else:
            day=13
    return str(day)+".09."+str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

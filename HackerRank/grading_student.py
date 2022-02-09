#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def generate_five_multiple(num):
    while num%5!=0:
        num+=1
    return num
        
def gradingStudents(grades):
    for grade in grades:
        next_five_multiple=generate_five_multiple(grade)
        if grade<38:
            print(grade)
        elif next_five_multiple-grade<3:
            print(next_five_multiple)
        else:
            print(grade)
                
                
                
            
if __name__ == '__main__':
    grades=[]
    grades_count=int(input())
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

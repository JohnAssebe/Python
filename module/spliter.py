# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 00:05:58 2019

@author: Yohannes Assebe
"""
john=open("John.txt")
for each_line in john:
     (name,speech)=each_line.split(';')
     print(name)
     print("\t\t","says")
     print(speech)
john.close()

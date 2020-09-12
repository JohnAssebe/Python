# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:42:16 2019

@author: Yohannes Assebe
"""
def nested_list(k,indent=0,booleanValueToIndent=True):
        for i in k:
           if (isinstance(i,list)):
               #print(indent*" ",end='')
               if booleanValueToIndent:
                       nested_list(i,indent+1,booleanValueToIndent)
               else:
                      nested_list(i,0,booleanValueToIndent) 
               
           else:
               if booleanValueToIndent:
                       for z in range(indent):
                                       print("\t",end='')
               print(i)

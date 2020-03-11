# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:30:26 2019

@author: Yohannes Assebe
"""
import csv 
from matplotlib import pyplot as plt
plt.title("Africa Annual Inflation per years")
#print(plt.style.available)
#plt.style.use("seaborn-notebook")
with open("african_crises.csv") as af:
    files=csv.DictReader(af)
    x=[]
    y=[]
    for row in files:
        x.append(int(row['year']))
        y.append(float(row['inflation_annual_cpi']))
    plt.scatter(x,y)
    plt.scatter(x[1],y[1])
    
        
       
    
    

plt.xlabel("Year")
plt.ylabel("Annual Inflation")
plt.grid(True)

#plt.legend()
#plt.ylim(0,100)
plt.tight_layout()
#print(plt.style.available)
plt.savefig("AffricaAnnualInflations.png")
plt.show()


import pandas as pd 

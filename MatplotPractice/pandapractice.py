# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 04:08:28 2019

@author: Yohannes Assebe(John)
"""
import pandas as pd
import matplotlib.pyplot as plt 
countryName=[]
file=pd.read_csv("african_crises.csv")
file.hist(bins=50, figsize=(10,30))
#if file['country'] not in countryName:
#    countryName.append(file['country'])
#for k in countryName:
#    plt.plot(file['year'],file['inflation_annual_cpi'],label=countryName)
#plt.legend(loc="upper left")
#plt.show()



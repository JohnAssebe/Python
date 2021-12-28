# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 04:52:21 2019

@author: Yohannes Assebe(John)
"""

from matplotlib import pyplot as plt
plt.title("Africa Annual Inflation per years")
#print(plt.style.available)
plt.style.use("seaborn-notebook")
listOffile=[]
countryName=[]
year=[]
annualInflation=[]
initial=0
with open("african_crises.csv") as af:
    for k in af:
        listOffile.append(af.readline())
    for k in range(len(listOffile)):
        files=listOffile[k].split(",")
        if files[2] not in countryName:
            countryName.append(files[2])
    for a in countryName:
        year.append([])
        annualInflation.append([])
    while(initial<len(countryName)-1):
            for b in range(len(listOffile)):
                  files=listOffile[b].split(",")
                  if countryName[initial]!=files[2]:
                      initial+=1
                  year[initial].append(int(files[3]))
                  annualInflation[initial].append(float(files[9]))
                      
for i in range(len(countryName)):
    x_value=year[i]
    y_value=annualInflation[i]
    plt.plot(x_value,y_value,label=countryName[i],linewidth=2)
    

plt.xlabel("Year")
plt.ylabel("Annual Inflation")
plt.grid(True)
plt.legend()
plt.ylim(0,1000)
plt.tight_layout()
#print(plt.style.available)
plt.savefig("AffricaAnnualInflations.png")
plt.show()

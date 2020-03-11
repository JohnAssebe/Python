# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 01:40:39 2019

@author: Yohannes Assebe(John)
"""
import matplotlib.pyplot as plt
plt.title("Pie chart Graph")
slices=["john","Ermi","Assebe","skuar"]
values=[100000,29000,195000,35000]
explode=[0.1,0,0,0]
#To rotate we can set a startangele=90 or any angle we want to rotate
#To use a percent we should use autopct=%1.1f%% 
plt.pie(values,labels=slices,
        explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,
        autopct='%1.1f%%',
        startangle=0)
plt.tight_layout()
plt.show()


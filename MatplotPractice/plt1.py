# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 04:22:38 2019

@author: Yohannes Assebe(John)
"""
import numpy as np
import matplotlib.pyplot as plt
from pylab import show
plt.title("Sin(x) graph")
x=np.arange(0,10,0.1)
y=np.sin(x)
plt.plot(x,y)
show()
plt.title("Absolute value graph")
t=np.arange(-10,10,1)
a=np.abs(t)
plt.plot(t,a)
show()

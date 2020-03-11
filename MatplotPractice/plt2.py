# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 05:38:07 2019

@author: Yohannes Assebe
"""
import random as ra
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
#==================step1: create Figure===============================
fig=Figure(figsize=(12,8),facecolor='white')
#==================step2:add subplot==================================
axis1=fig.add_subplot(211)
#==================step3:set xvalue and yvalues=======================
xvalue=[ra.randint(0,10),ra.randint(0,10),ra.randint(0,10),ra.randint(0,10)]
yvalue=[ra.randint(0,10),ra.randint(0,10),ra.randint(0,10),ra.randint(0,10)]
#==================step4:plot x and y values in the created axis======
axis1.plot(xvalue,yvalue)
axis1.grid(linestyle="-")
#==================step5:add horizontal and vertical labels===========
axis1.set_xlabel("Horizontal value")
axis1.set_ylabel("Vertical value")

axis2=fig.add_subplot(212)
xvalue2=[1,2,3,4]
yvalue2=[0,7,8,9]
axis2.plot(xvalue2,yvalue2)
axis2.grid(linestyle="")
axis2.set_xlabel("Horizontal value")
axis2.set_ylabel("Vertical value")   

#==================step6:create an instance of main frame=================
win=tk.Tk()
#==================step7:set the figure in the main frame=================
figurec=FigureCanvasTkAgg(fig,master=win)
figurec._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)

win.mainloop()


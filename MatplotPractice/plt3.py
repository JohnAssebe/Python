# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 06:32:37 2019

@author: Yohannes Assebe(John)
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
fig=Figure(figsize=(10,10),facecolor='White')

axis=fig.add_subplot(111)
xvalues=[1,2,3,4,5]
yvalue0=[5,0,8,7,4]
yvalue1=[3,2,1,2.1,1]
yvalue2=[3,3,5,600,5]
t0, =axis.plot(xvalues,yvalue0)
t1, =axis.plot(xvalues,yvalue1)
t2, =axis.plot(xvalues,yvalue2)
axis.set_ylim(0,9)
axis.set_xlabel("Horizontal Value")
axis.set_ylabel("Vertical Value")
axis.grid()
fig.legend((t0,t1,t2),('First ','Second','Third'),'upper left')
win=tk.Tk()
win.withdraw()
canvas=FigureCanvasTkAgg(fig,master=win)
canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
win.update()
win.deiconify()
win.mainloop()


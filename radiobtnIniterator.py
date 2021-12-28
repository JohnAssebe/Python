import tkinter as tk
from tkinter import ttk
'''
author: (John)Yohannes Assebe
The only thing we need to add is the name of color in a list item to add radio btn as well as its handler.
'''
win=tk.Tk()
color=["Red","Green","Blue","White","Gray","Gold","Yellow","Alice blue"]
var1=tk.IntVar()
win.title("Iterator App")
win.resizable(0,0)
def Rbtnclicked():
    win.configure(background=color[var1.get()])
    lab.configure(text="Color changed to :"+color[var1.get()])
for num in range(len(color)):
     radio=tk.Radiobutton(win,text=color[num],value=num,variable=var1,command=Rbtnclicked)
     radio.grid(column=num,row=1)
     

#Label creation
lab=ttk.Label(win,text="Color Change")
lab.grid(column=4,row=3,sticky=tk.W)

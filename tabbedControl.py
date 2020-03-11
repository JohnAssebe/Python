import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("Tabbed Control")
#create a tab control

tabcontrol=ttk.Notebook(win)
tab1=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="Tab1")
tab2=ttk.Frame(tabcontrol)
tab2=ttk.Frame(tab2,bg='blue')
tabcontrol.add(tab2,text="Tab2")
for i in range(5):
        canvas=tk.Canvas(tab2,width=i+50,height=i+50,bg="red")
        canvas.grid(column=i,row=i)
for i in range(4):
        canvas=tk.Canvas(tab2,width=i+50,height=i+50,bg="red")
        canvas.grid(column=i+1,row=i)
for k in range(4,-1,-1):
      canvas=tk.Canvas(tab2,width=i+50,height=i+50,bg="blue")
      canvas.grid(column=4+(5-k),row=k)
for k in range(4,-1,-1):
      canvas=tk.Canvas(tab2,width=i+50,height=i+50,bg="blue")
      canvas.grid(column=3+(5-k),row=k)
tabcontrol.pack(expand=1,fill="both")
win.mainloop()

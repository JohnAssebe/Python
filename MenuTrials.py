import tkinter as tk
from tkinter import Menu


win=tk.Tk()
win.title("Menu Trial")
menubar=Menu(win)
win.configure(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
helpmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="New",menu=filemenu)
menubar.add_cascade(label="Help",menu=helpmenu)



filemenu.add_command(label="File")
filemenu.add_command(label="Object")
filemenu.add_command(label="Class")


helpmenu.add_command(label="About Us")

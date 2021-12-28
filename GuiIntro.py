# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:34:50 2019

@author: John(Yohannes Assebe)
"""
import tkinter as tk
from tkinter import ttk
def btnClicked():
    btn.configure(text='clicked!',state='disabled')
    lab.configure(text="Hi Welcome  "+name.get(),foreground='blue')
win=tk.Tk()
win.title("First App")
#win.resizable(0,0)

lab=ttk.Label(win,text="Enter Your Name:")
lab.grid(column=1,row=1)  
#this code creates text box 
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=15,textvariable=name)
nameEntered.grid(column=1,row=2)
#this code creates a button
btn=ttk.Button(win,text="clickMe",command=btnClicked)
btn.grid(column=1,row=3)
'''We can write all of our GUI code in advance and nothing will be displayed on
the user's screen until we call this endless loop'''
nameEntered.focus()
tk.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:34:50 2019

@author: John(Yohannes Assebe)
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
win=tk.Tk()
#it reads an ico extension pics set the full path location for it to be displayed as an icon
#win.iconbitmap(r'C:\Users\User1\AppData\Local\Programs\Opera\63.0.3368.71\resources\AD2FD2BD-0727-4AF7-8917-AAED8627ED47.ico')
color=["gray","alice blue","white"]

def radPressed():
    labelframe.configure(text=color[radVar.get()])

def btnClicked():
    btn.configure(text='clicked!',state='disabled')
    #name is Module level variable
    lab.configure(text="Hi Welcome  "+name.get(),foreground='blue')
    drop.configure(state='disabled')
    nameEntered.configure(state='disabled')
    #number is Module level variable
    infoAge.configure(text="You Are "+number.get(),foreground='blue')
def _messageAbout():
    win.withdraw()
    mBox.showinfo("About","This is the program used to create a radio button change a text in a label")
    #mBox.showwarnning("About","This is the program used to create a radio button change a text in a label")
    #mBox.showinfo("About","This is the program used to create a radio button change a text in a label")
    #answer=mBox.askyesno("About","This is th program used to create a radio button change a text in a label")
    #print(answer)
def _spin():
    value=spin.get()
    scrolltext.insert(tk.INSERT,value+'\n')
    #print(value)
def _quitWindow():
    win.quit()
    win.destroy()
    exit()
win.title("Welcome App")
#add menubar,menu,and menu item in the created menu

menubar=Menu(win)
win.configure(menu=menubar)
#add menu item
filemenu=Menu(menubar,tearoff=0)
helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Help",menu=helpmenu)

#add menu item
helpmenu.add_command(label="about",command=_messageAbout)
filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=_quitWindow) 
#make window size not resizable

#win.resizable(0,0)
#create a tab control

tabcontrol=ttk.Notebook(win)
tab1=ttk.Frame(tabcontrol)
tab2=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="Tab1")
tabcontrol.add(tab2,text="Tab2")
tabcontrol.pack(expand=1,fill="both")



#Label creation
lab=ttk.Label(tab1,text="Enter Your Name:")
lab.grid(column=1,row=1)  

#create text box 
name=tk.StringVar()
nameEntered=ttk.Entry(tab1,width=15,textvariable=name)
nameEntered.grid(column=1,row=2)

#Label to give information 
infoAge=ttk.Label(tab1,text="     Choose Your age(15-20)")
infoAge.grid(column=2,row=1)

#drop down combo box
number=tk.StringVar()
drop=ttk.Combobox(tab1,width=12,textvariable=number,state='readonly')
drop['value']=(15,16,17,18,19,20)
drop.current(0)
drop.grid(column=2,row=2)

#create 3 check button with different state
#observe that are from 'tk' not from 'ttk'(themed tkinter) 
var=tk.IntVar()
chbtn=tk.Checkbutton(tab2,text="Disable",variable=var,state='disabled')
chbtn.select()
chbtn.grid(column=0,row=1,sticky=tk.W)

var2=tk.IntVar()
chbtn2=tk.Checkbutton(tab2,text="Unchecked",variable=var2)
chbtn2.grid(column=1,row=1,sticky=tk.W)
chbtn2.deselect()

var3=tk.IntVar()
chbtn3=tk.Checkbutton(tab2,text="checked",variable=var3)
chbtn3.select()
chbtn3.grid(column=2,row=1,sticky=tk.W)

#create radio button
#observe that are from 'tk' not from 'ttk'(themed tkinter)
radVar=tk.IntVar()
rad1=tk.Radiobutton(tab2,text=color[0],variable=radVar,value=0,command=radPressed)
rad1.grid(column=0,row=2,sticky=tk.W)

rad2=tk.Radiobutton(tab2,text=color[1],variable=radVar,value=1,command=radPressed)
rad2.grid(column=1,row=2,sticky=tk.W)

rad3=tk.Radiobutton(tab2,text=color[2],variable=radVar,value=2,command=radPressed)
rad3.grid(column=2,row=2,sticky=tk.W)


#create a button
btn=ttk.Button(tab1,text="submit",command=btnClicked)
btn.grid(column=3,row=2)

#create scrolled text observe the import 
scrolltext=scrolledtext.ScrolledText(tab1,width=35,height=3,wrap=tk.WORD)
scrolltext.grid(column=0,columnspan=3)
#make cursor (at the beginning of the GUI) in text box
nameEntered.focus()
#LabelFrame
labelframe=ttk.LabelFrame(tab2,text="Main Label Frame")
labelframe.grid(column=1,row=5)
labels1=ttk.Label(labelframe,text="Label1")
labels1.grid(column=0,row=0)
labels2=ttk.Label(labelframe,text="Label2")
labels2.grid(column=1,row=0)
labels3=ttk.Label(labelframe,text="Label3")
labels3.grid(column=2,row=0)
#create spinbox to tab2
spin=ttk.Spinbox(tab2,width=5,from_=0,to=10,state="readonly",command=_spin)
spin.grid(column=0,row=4,sticky=tk.W)
'''We can write all of our GUI code in advance and nothing will be displayed on
the user's screen until we call this endless loop'''
tk.mainloop()

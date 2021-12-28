from tkinter import *
from DBconfig import mysqlconfig
import mysql.connector as mysql
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mbox
import BookModel
import os 
print(os.path)
win=Tk()
win.title("Boook")
##a=BookModel.Model()
##a.useDB("firstpythondb")    
    
#===============variables To User Input for Entry Part=========
inserttitle=StringVar()
gettitle=StringVar()
modifytitle=StringVar()
#===============variables To User Input for Page Part=========
insertpage=IntVar()
getpage=IntVar()
modifypage=IntVar()

def insert():
    title=inserttitle.get()
    page=insertpage.get()
    quote=scrolledtxt.get(1.1,END)
    model=BookModel.Model()
    model.useDB("firstpythondb")
    model.insertBook(title,page,quote)
    scrolledtxt.insert(INSERT,"")
    model.close()
    
   
def showall():
    title=gettitle.get()
    model=BookModel.Model()
    model.useDB("firstpythondb")
    books=model.showBooks(title)
    page=books[0][2]
    quotes=model.showQuote(page)
    scrolledtxt.insert(INSERT,books)
    scrolledtxt.insert(INSERT,quotes)
def modify():
    title=modifytitle.get()
    page=modifypage.get()
    quote=scrolledtxt.get(1.0,END)
    model=BookModel.Model()
    model.useDB("firstpythondb")
    model.updateBooks(title,page)

#================TabControl===================
tabcontrol=ttk.Notebook(win)
Guitab=ttk.Frame(tabcontrol)
Widget=ttk.Frame(tabcontrol)
tabcontrol.add(Guitab,text="Gui DB")
tabcontrol.add(Widget,text="Widgets")
tabcontrol.pack(fill=BOTH,expand=1)
##labelFrame=LabelFrame(Guitab)
##labelFrame.grid(column=0,row=0)
#===============Label==========================
Label(Guitab,text="Book Title",fg="Blue").grid(column=0,row=1)
Label(Guitab,text="page",fg="Blue").grid(column=1,row=1)
#========Entry,and btn=========================
insertEntry=Entry(Guitab,textvariable=inserttitle)
insertEntry.grid(column=0,row=2,padx=12,pady=3)
insertPageEntry=Entry(Guitab,textvariable=insertpage,width=5)
insertPageEntry.grid(column=1,row=2,padx=12,pady=3)
insertbtn=Button(Guitab,text="Insert Quote",bd=3,command=insert)
insertbtn.grid(column=2,row=2,padx=12,pady=3)
#========Entry,and btn=========================

getEntry=Entry(Guitab,textvariable=gettitle)
getEntry.grid(column=0,row=3,padx=12,pady=3)
getPageEntry=Entry(Guitab,textvariable=getpage,width=5)
getPageEntry.grid(column=1,row=3,padx=12,pady=3)
getbtn=Button(Guitab,text="Get  Quotes",bd=3,command=showall)
getbtn.grid(column=2,row=3,padx=12,pady=3)
#========Entry,and btn=========================
modifyEntry=Entry(Guitab,textvariable=modifytitle)
modifyEntry.grid(column=0,row=4,padx=12,pady=3)
modifyPageEntry=Entry(Guitab,textvariable=modifypage,width=5)
modifyPageEntry.grid(column=1,row=4,padx=12,pady=3)
modifybtn=Button(Guitab,text="Modify Quote",bd=3,command=modify)
modifybtn.grid(column=2,row=4,padx=12,pady=3)
#==============Label===========
Label(Guitab,text="Book Quotation",fg="Blue").grid(column=0,row=5)
#==============scrolledtext=================
scrolledtxt=scrolledtext.ScrolledText(Guitab,width=40,height=5,wrap=WORD)
scrolledtxt.grid(column=0,columnspan=4,padx=12,pady=3)



win.mainloop()

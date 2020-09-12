'''
@Author:Yohannes Assebe
The Program will merge two or more pdfs 
'''
from tkinter import *
import tkinter.filedialog as tkf
from tkinter import messagebox
import PyPDF2
import re
tk=Tk()
tk.title("App for Merging Pdf files")
tk.minsize(650,500)
name=[]
try:
    file=tkf.askopenfiles(title="Select morethan 1 PDF")
    tk.withdraw()
    writer=PyPDF2.PdfFileWriter()
    for i in file:
        name.append(i.name)
    for i in range(len(name)):
        file=open(name[i],'rb')
        read_file=PyPDF2.PdfFileReader(file)
        for i in range(read_file.numPages):
            obj=read_file.getPage(i)
            writer.addPage(obj)
    
    start_index=name[0].rfind("/")
    last_index=name[0].rfind(".")
    names =name[0][start_index+1:last_index]+"_and_"+str(len(name)-1)+"other(s) books"
    writer.write(open(f"{names}.pdf",'wb'))
    messagebox.showinfo("Success Message",f"Thanks for using this App {names}.pdf is created in your working directory")
except IndexError as err:
    messagebox.showwarning("Error","Please use more than one pdf to merge succesfully")
except PyPDF2.utils.PdfReadError as err:
    messagebox.showwarning("Error","File Error Select only PDF files")
    
    

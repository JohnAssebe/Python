'''
@Author:Yohannes Assebe(John Assebe githubAccount)
This program encrypt PDF
'''
from tkinter import *
import PyPDF2
import subprocess
import tkinter.filedialog as tkfd
tk=Tk()
tk.title("Encrypter")
tk.minsize(600,200)
tk.resizable(0,0)
password=StringVar()
def openfile():
    file=tkfd.askopenfile(title="please select pdf file to be encrypted")
    filereader=PyPDF2.PdfFileReader(file.name,'rb')
    filewriter=PyPDF2.PdfFileWriter()
    for i in range(filereader.numPages):
        filewriter.addPage(filereader.getPage(i))
    index_start=file.name.rfind('/')
    last_index=file.name.rfind('.')
    final_file_name=str(file.name[index_start+1:last_index])
    result=open(final_file_name+'.pdf','wb')
    return filewriter,result,final_file_name
def Submit():
    filewriter.encrypt(password.get())
    filewriter.write(result)
    result.close()
    subprocess.Popen(['start',str(final_file_name)+".pdf"],shell=True)
lab=Label(tk,text="Encrypt Your PDF")
lab.grid(column=1,row=1)
lab1=Label(tk,text="Password:",width=30)
lab1.grid(column=0,row=2)
entry=Entry(tk,width=30,textvariable=password)
entry.grid(column=1,row=2)
openbutton=Button(tk,text="Submit",command=Submit)
openbutton.grid(column=1,row=4)
if __name__=="__main__":
    (filewriter,result,final_file_name)=openfile()
    
    
    


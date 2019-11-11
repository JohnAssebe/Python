'''
created at 1:26 AM 11/7/2019
For different password usage there is also different encrypted file is generated in this program
password based hashing algorithm used in this program
'''
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.filedialog as tkf
from tkinter import scrolledtext
from tkinter import messagebox as mb
import base64
#These cryptography Modules are used to encrypt the text file based on
#the password provided in the text entry 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import os
win=tk.Tk()
win.minsize(500,500)
win.resizable(0,0)
PrimaryKey=tk.StringVar()
PrimaryKeyDecryption=tk.StringVar()
encriptedtxt=b''
salt=b''
win.title("Digital Signature")
def Reader(file):
    try:
            with open(file) as f:
                fil=f.read()
                return fil
    except:
        mb.showinfo("Invalid File","Select A \"text\" or \".py\"  or \"and related files\" files to ")
def openfile():
    files=tkf.askopenfile()
##    scrolltxt2.delete("1.0",tk.END)
##    scrolltxt2.insert(tk.INSERT,Reader(files.name))
    password_provided=PrimaryKey.get()
    password=password_provided.encode()
    global salt
    salt=os.urandom(16)
    kdf=PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
    
    key=base64.urlsafe_b64encode(kdf.derive(password))
    print(key)
    try:
        txtfile=Reader(files.name)
        txtfile=txtfile.encode()
        f=Fernet(key)
    
        global encriptedtxt
        encriptedtxt=f.encrypt(txtfile)
        
        scrolltxt.delete("1.0",tk.END)
        scrolltxt.insert(tk.INSERT,encriptedtxt)
        
        with open("encription.txt","w") as encript:
                encript.write(scrolltxt.get("1.0",tk.END))
            
    except:
        print("Invalid File Input")
    
        
    
    
def sent():
    pass
def Decrypt():
    try:
            scrolltxt_d.delete("1.0",tk.END)
            password=PrimaryKeyDecryption.get()
            passwords=password.encode()
            global salt
            kdf=PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
            )
            key_d=base64.urlsafe_b64encode(kdf.derive(passwords))
            f2=Fernet(key_d)
          
            #print(encriptedtxt)
            decryptedtxt=f2.decrypt(encriptedtxt)
            scrolltxt_d.delete("1.0",tk.END)
            scrolltxt_d.insert(tk.INSERT,decryptedtxt)
    except:
        mb.showinfo("Input Error","INCORRECT PASSWORD INPUT TO DECRYPT")
        
tabcontrol=ttk.Notebook(win)
tab1=ttk.Frame(tabcontrol)
tab2=ttk.Frame(tabcontrol)
tab3=ttk.Frame(tabcontrol)
tab4=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="Choose File")
tabcontrol.add(tab2,text="Encrypted File")
##tabcontrol.add(tab3,text="Original File")
tabcontrol.add(tab4,text="Decrypt File")
tabcontrol.pack(expand=1,fill="both")

label1=ttk.Label(tab1,text="Enter your preffered public key",font=("Helvetica", 12, "bold"))
label1.grid(column=0,row=0,padx=20,pady=20)
label1.place(x=100,y=120)
entry=ttk.Entry(tab1,textvariable=PrimaryKey,font=("Helvetica", 10, "bold"))
entry.grid(column=0,row=1,padx=20)

entry.place(x=160,y=160)
label2=ttk.Label(tab1,text="Choose the file to encrypt",font=("Helvetica", 12, "bold"))
label2.grid(column=0,row=2,padx=20,pady=20)
label2.place(x=100,y=200)
btn=ttk.Button(tab1,text="Browse",command=openfile)
btn.grid(column=0,row=3,padx=20)
btn.place(x=185,y=240)

scrolltxt=scrolledtext.ScrolledText(tab2,width=60,height=24,wrap=tk.WORD)
scrolltxt.grid(column=0,row=0)
btn2=ttk.Button(tab2,text="Send",command=sent)
btn2.grid(column=0,row=1,padx=20)
btn2.place(x=400,y=400)


##scrolltxt2=scrolledtext.ScrolledText(tab3,width=60,height=20,wrap=tk.WORD)
##scrolltxt2.grid(column=0,row=0)
##btn3=ttk.Button(tab3,text="Send",command=sent)
##btn3.grid(column=0,row=1,padx=20)
##btn3.place(x=400,y=350)
label_d=ttk.Label(tab4,text="Enter the key to decrypt file",font=("Helvetica", 12, "bold"))
label_d.grid(column=0,row=0,padx=20,pady=20)
label_d.place(x=100,y=40)
entry_d=ttk.Entry(tab4,textvariable=PrimaryKeyDecryption,font=("Helvetica", 10, "bold"))
entry_d.grid(column=0,row=1,padx=20)
entry_d.place(x=150,y=90)
scrolltxt_d=scrolledtext.ScrolledText(tab4,width=60,height=20,wrap=tk.WORD)
scrolltxt_d.grid(column=0,row=2)
scrolltxt_d.place(x=0,y=120)
btn_d=ttk.Button(tab4,text="Decrypt",command=Decrypt)
btn_d.grid(column=0,row=3,padx=20)
btn_d.place(x=400,y=450)
win.mainloop()


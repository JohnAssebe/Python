'''
@author :John Assebe(Yohannes Assebe)
created on 12:05 PM 11/9/2019

'''
#Inorder to run this program A connection is needed else socket.gaierror error is created
import smtplib
import tkinter as tk
from tkinter import ttk
win=tk.Tk()
gmail=tk.StringVar()
password=tk.StringVar()
win.title("Send Mail")
def sent():
        #login by using username and password
    smtpobj.login(f"{gmail}",f"{password}")
    #send message sender address,receiver address and Subject to fill messsage body -
    #respectively 
    smtpobj.sendmail("johnassebe@gmail.com","johnshimelis09@gmail.com","Subject:\n John I would like to thank you for all you have done to me")
    #quit the connection to the server
    smtplib.quit()
label_e=ttk.Label(win,text="Enter Your Gmail Account")
label_e.grid(column=0,row=0)
entry_e=ttk.Entry(win,textvariable=gmail)
entry_e.grid(column=0,row=1)
label_p=ttk.Label(win,text="Enter Your Gmail Password")
label_p.grid(column=0,row=2)
entry_p=ttk.Entry(win,textvariable=password)
entry_p.grid(column=0,row=3)
#step1:Create smtp object
#if This is not valid to create the object use SSL encryption  (smtplib.SMTP_SSL("smtp.gmail.com",465)
#"smtp.gmail.com" server domain name for gmail check for other
smtpobj=smtplib.SMTP("smtp.gmail.com",587)
#create a hello greeting for the server
smtpobj.ehlo()
#we should start tls encryption(skip this step if it is SSL)
smtpobj.starttls()
btn=ttk.Button(win,text="sent",command=sent)
btn.grid(column=0,row=10)


smtpobj.quit()

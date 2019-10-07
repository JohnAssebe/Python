"""
@author:John(Yohannes Assebe)
created at 5:58 AM 10/5/2019
simple calculator
"""
from tkinter import *
print('''\
    Yohannes Assebe
    @AAIT(Addis Ababa university of Technology)
''')

win=Tk()
win.title("#___Calculator___#")
win.resizable(0,0)
#win.iconbitmap(r"C:\Users\User1\Desktop\PythonPractice\GUI\Projects\icon\calculator_log_from_anaconda.ico")
num=StringVar()

value=""
def action(num_a):
    global value
    value+=str(num_a)
    num.set(value)
def clearbtnhandler():
    global value
    value=""
    num.set(value)
def equalbtnhandler():
    try:
        global value
        #to prevent error display if '=' sign first pressed  
        if(num.get()!=''):
            value=str(eval(num.get()))
            num.set(value)
        else:
            value=""
            num.set(value)
            
    except ZeroDivisionError:
       value="Division by 0 is invalid"
       num.set(value)
def backspacehandler():
   global value
   value=value[0:len(value)-1]
   num.set(value)
def forwardhandler():
   global value
   value=value[0:len(value)]+value[-1]
   num.set(value)
def percenthandler():
    global value
    value=str(eval(num.get()+"/"+"100"))
    num.set(value)
#====================Frame=================
Top=Frame(win,width=400,height=90)
Top.pack(side=TOP)
Middle=Frame(win,width=400,height=700)
Middle.pack(expand=1,fill="both")
#===================Label and text box on the Top frame==================
##lbl=Label(Top,text="Calculator",font=("arial",10,"bold"),bd=10,fg="Blue")
##lbl.grid(column=0,row=0)
txt=Entry(Top,text="",textvariable=num,font=("arial",15,"bold"),bd=20,fg="Blue")
txt.grid(column=0,row=1)

#===================7,8,9 btns in the Middle Frame===============
btn7=Button(Middle,text="7",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(7))
btn7.grid(column=0,row=0)
btn8=Button(Middle,text="8",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(8))
btn8.grid(column=1,row=0)
btn9=Button(Middle,text="9",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(9))
btn9.grid(column=2,row=0)

#===================4,5,6 btns==================
btn4=Button(Middle,text="4",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(4))
btn4.grid(column=0,row=1)
btn5=Button(Middle,text="5",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(5))
btn5.grid(column=1,row=1)
btn6=Button(Middle,text="6",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(6))
btn6.grid(column=2,row=1)

#===================0,1,2,3 btns=============
btn1=Button(Middle,text="1",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(1))
btn1.grid(column=0,row=2)
btn2=Button(Middle,text="2",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(2))
btn2.grid(column=1,row=2)
btn3=Button(Middle,text="3",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(3))
btn3.grid(column=2,row=2)
btn0=Button(Middle,text="0",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=lambda:action(0))
btn0.grid(column=1,row=3)
#===================operation btns=============
plusbtn=Button(Middle,text="+",bd=5,font=("arial",15,"bold"),padx=15,pady=10,bg="black",fg="white",command=lambda:action("+"))
plusbtn.grid(column=3,row=0)
minusbtn=Button(Middle,text="-",bd=5,font=("arial",18,"bold"),padx=15,pady=10,bg="black",fg="white",command=lambda:action("-"))
minusbtn.grid(column=3,row=1)
multiplybtn=Button(Middle,text="x",bd=5,font=("arial",15,"bold"),padx=15,pady=10,bg="black",fg="white",command=lambda:action("*"))
multiplybtn.grid(column=3,row=2)
divisionbtn=Button(Middle,text="/",bd=5,font=("arial",18,"bold"),padx=15,pady=10,bg="black",fg="white",command=lambda:action("/"))
divisionbtn.grid(column=3,row=3)
#===================<,>,%,. btns=============
backspacebtn=Button(Middle,text="<",bd=5,bg="orange",fg="white",font=("arial",15,"bold"),padx=15,pady=10,command=backspacehandler)
backspacebtn.grid(column=0,row=3)
forwardbtn=Button(Middle,text=">",bd=5,bg="orange",fg="white",font=("arial",15,"bold"),padx=15,pady=10,command=forwardhandler)
forwardbtn.grid(column=2,row=3)
dotbtn=Button(Middle,text=".",bd=5,font=("arial",16,"bold"),padx=15,pady=10,bg="black",fg="white",command=lambda:action("."))
dotbtn.grid(column=2,row=4)
percentbtn=Button(Middle,text="%",bd=5,font=("arial",15,"bold"),padx=15,pady=10,bg="black",fg="white",command=percenthandler)
percentbtn.grid(column=1,row=4)
#==================== =,c btns =================
clearbtn=Button(Middle,text="C",bg="red",fg="white",bd=5,font=("arial",15,"bold"),padx=15,pady=10,command=clearbtnhandler)
clearbtn.grid(column=0,row=4)
equalbtn=Button(Middle,text="=",bd=5,font=("arial",18,"bold"),bg="blue",fg="white",padx=15,pady=10,command=equalbtnhandler)
equalbtn.grid(column=3,row=4)
win.mainloop()

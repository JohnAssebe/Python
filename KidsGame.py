'''
@Author:Yohannes Assebe(John Assebe)
written @ 4:25 PM 3/6/2020
A kids game by level to practice math
press Enter or Button to check your answer 
'''

from tkinter import *
from tkinter import messagebox as mBox
import random as ra
import threading 
import time
import sys
#the class that init the Game
class Win1:
    def __init__(self,root):
        self.root=root
        time_thread=threading.Thread(target=self.remain_time)
        time_thread.start()
        score_label=Label(self.root,text="Score:"+str(score),font="Verdana 30 bold").grid(column=3,row=0)
        self.level_selector()
        entry=Entry(self.root,textvariable=question,state="disabled",font="Verdana 30 bold",fg="green")
        entry.grid(column=0,row=1,padx=10,pady=10,columnspan=5)
        answer_entry=Entry(self.root,textvariable=answer,font="Verdana 30 bold")
        answer_entry.bind('<Return>',self.onEnter)
        
        
        answer_entry.grid(column=0,row=2,padx=10,pady=10,columnspan=5)
        answer_entry.focus()
        answer.set("              ")
        self.btn=Button(self.root,text="Answer",command=self.check_answer,font="Arial 20 bold")
        self.btn.grid(column=1,row=3)
    def onEnter(self,*args):
        self.check_answer()
        
    #selects other Window if Game is over
    def window_chooser(self,_class):
        try:
            if self.new.state=='normal':
                self.new.focus()
        except:
            self.root.withdraw()
            self.new=Toplevel(self.root)
            _class(self.new)
    # display the remaining time
    def remain_time(self):
        global t
        while t>-1:
            m,s=divmod(t,60)
            h,m=divmod(m,60)
            t-=1
            time.sleep(1)
            remain=str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
            label=Label(self.root,text=remain,font="Verdana 30 bold").grid(column=0,row=0)
            if remain=="00:00:00":
                self.window_chooser(Win2)

    
    # check the answer is  right or not,increment score by one if right 
    #and set the button green if the answer is right or red if the answer is wrong
    def check_answer(self):
        real_answer=eval(question.get())
        try:
            if round(float(real_answer),2)==round(float(answer.get()),2):
                global t
                t=15
                self.btn.configure(foreground='green')
                global score
                score+=1
                Label(self.root,text="Score:"+str(score),font="Verdana 30 bold").grid(column=3,row=0)
                self.level_selector()
                
            else:
                self.btn.configure(fg='red')
                #Label(self.root,text="Score:"+str(score),font="Verdana 30 bold").grid(column=3,row=0)
           
            answer.set("              ")
        except ValueError:
            answer.set("              ")
  #generate a random question based on level 
    def random_question_generator(self,level='easy',start=1,end=50,oper_strt=0,oper_end=1):
        if level=='easy':
            num1=ra.randint(start,end)
            num2=ra.randint(start,end)
            operatorRand=ra.randint(oper_strt,oper_end)
            operations=(["+","-","*","/"])
            return "             "+str(num1)+operations[operatorRand]+str(num2)
        #when the level reaches medium it will generate three numbers 
        elif level=='medium':
            global t
            t=30
            num1=ra.randint(start,end)
            num2=ra.randint(start,end)
            num3=ra.randint(start,end)
            operatorRand=ra.randint(oper_strt,oper_end)
            operations=(["+","-","*","/"])
            return "             "+str(num1)+operations[operatorRand]+str(num2)+operations[operatorRand]+str(num3)
            
            
            
    #selects the level based on the score 
    def level_selector(self):
        global score
        if score<5:
            while True:
                  question_generated=self.random_question_generator()
                  if int(eval(question_generated))>=0:
                    global question
                    question.set(question_generated)
                    break
        if score>=5:
            while True:
                  question_generated=self.random_question_generator(start=50,end=101)
                  if int(eval(question_generated))>=0:
                     question.set(question_generated)
                     break
        if score>=10:
             while True:
                  question_generated=self.random_question_generator(start=1,end=11,oper_strt=2,oper_end=3)
                  if float(eval(question_generated))==int(eval(question_generated)):
                    question.set(question_generated)
                    break 
        if score>=15:
            while True:
                  question_generated=self.random_question_generator(start=2,end=101,oper_strt=3,oper_end=3)
                  if float(eval(question_generated))==int(eval(question_generated)):
                     question.set(question_generated)
                     break
        if score>=30:
            question_generated=self.random_question_generator(level='medium',start=50,end=101)
            question.set(question_generated)
            
#the second window   
class Win2:
    def __init__(self,root):
        self.root=root
        self.root.minsize(width=400,height=300)
        self.root.resizable(0,0)
        global score
        self.label=Label(self.root,text="Your Score:"+str(score),font="Verdana 30 bold",justify='center').grid(column=0,row=0,pady=5,padx=50)
        self.label=Label(self.root,text="Author: Yohannes Assebe(John)",font="Verdana 5",justify='center').grid(column=0,row=2,pady=50,padx=40)
        self.btn=Button(self.root,text="Continue",command=self.continue_game,font="Arial 20 bold")
        self.btn.grid(column=0,row=3,padx=0,pady=10)
        self.btn2=Button(self.root,text="Cancel",command=self.cancel_game,font="Arial 20 bold")
        self.btn2.grid(column=1,row=3,padx=10,pady=10)
    def window_chooser(self,_class):
        try:
            if self.new.state=='normal':
                self.new.focus()
        except:
            self.root.withdraw()
            global score,t
            score=0
            t=15
            self.new=Toplevel(self.root)
            _class(self.new)
    def continue_game(self):
        answer.set("              ")
        self.window_chooser(Win1)
        
        
    def cancel_game(self):
        self.root.quit()
        self.root.destroy()
        exit()
        
        
        
if __name__=='__main__':
    t=15
    score=0
    root=Tk()
    question=StringVar()
    answer=StringVar()
    app=Win1(root)
    root.title("Game for kids to practice math")
    root.resizable(0,0)
    root.mainloop()


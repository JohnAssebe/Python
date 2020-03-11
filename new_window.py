import tkinter as tk
class Win:
    def __init__(self,root):
        self.root=root
        self.root.geometry("400x400")
        self.root['bg']='coral'
        self.button_rename=tk.Button(self.root,text="Press Me",command=lambda:
        self.new_window(Win2)).pack() 
    def new_window(self,_class):
        try:
           if self.new.state=='normal':
               self.new.focus()
        except:
                self.new=tk.Toplevel(self.root)
                _class(self.new)
class Win2:
    def __init__(self,root):
        print(app.new.state())
        self.root=root
        self.root['bg']='navy'
        self.root.geometry("300x300+200+200")
        self.root['bg']='navy'
if __name__=="__main__":
    root=tk.Tk()
    app=Win(root)
    app.title="practice_open_two_windows"
    root.mainloop()
        

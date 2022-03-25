import os 
from languageTranslater import *
#from snippingTool import *
import snippingTool

from tkinter import *

import sys

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Write eng for english")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.b=Button(master,text="Pick language to copy, default english",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="copy",command=lambda: (os.system('python src\snippingTool.py'), (copyText(self.entryValue()))))
        self.b2.pack()
        self.b3=Button(master,text="copy and translate",command=lambda: (os.system('python src\snippingTool.py'), translate(copyText(self.entryValue()))))
        self.b3.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        try:
            return self.w.value
        except:
            return "eng"
            



        
if __name__ == '__main__':
    root = Tk()
    app = mainWindow(root)
    root.mainloop()

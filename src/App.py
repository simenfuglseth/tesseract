import os 
from languageTranslater import *
import keyboard 
from tkinter import *



class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)

        self.l=Label(top,text="Write ukr for ukrainian etc")
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

        self.l=Label(text="To translate non latin Alphabet languages click language.")
        self.l.pack()
        self.b=Button(master,text="language",command=self.popup)
        self.b.pack()
        self.b2=Button(master,text="copy",command=lambda: (os.system('python src\snippingTool.py'), (copyText(self.entryValue()))))
        self.b2.pack()
        #Added hotkey to copy text to clipboard
        keyboard.add_hotkey('F13', lambda: (os.system('python src\snippingTool.py'), (copyText(self.entryValue()))))
        self.b3=Button(master,text="copy and translate",command=lambda: (os.system('python src\snippingTool.py'), translate(copyText(self.entryValue()))))
        self.b3.pack()
        keyboard.add_hotkey('F14', lambda: (os.system('python src\snippingTool.py'), translate(copyText(self.entryValue()))))
        self.l.configure(font=("Helvetica", 12))

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








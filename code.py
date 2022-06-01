from datetime import datetime
from tkinter import * 
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('my clock')
label=Label(root,font=('ds-digital',80),background='black',foreground='white')
label.pack(anchor='center')
def getTime():
    now=datetime.now()
    t=now.strftime('%I:%M:%S %p %m/%d/%Y')
    label.config(text=t)
    label.after(1000,getTime)

getTime()
mainloop()
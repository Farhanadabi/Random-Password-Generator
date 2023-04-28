import random
import tkinter
import os,sys
from tkinter import END
import string
import time


chr=list('!@#*$')

let_up=list(string.ascii_uppercase)

let_low=list(string.ascii_lowercase)

dig=list(string.digits)

all = let_up+let_low+dig+chr

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def myappUi():
    global ent
    global lbl
    global scl
    
    myapp = tkinter.Tk()
    myapp.title("Random Password Generator")
    myapp.geometry('400x300')
    myapp.resizable(0,0)
    
    myapp.iconbitmap(resource_path('lock.ico'))
    myapp.config(bg="#12181E")
    tkinter.Label(myapp,text="Random Password Generator",font=("default",15),fg='#0288A3',bg='#12181E').pack(pady=8)
    
    ent = tkinter.Entry(myapp,width=22,state="normal",bg="gray",fg="#51E79D",justify="center")
    ent.pack(ipady=10,pady=20)

    scl = tkinter.Scale(myapp, from_=4, to=18,orient='horizontal', length= 130,bg='#12181E',fg='#51E79D',highlightbackground='#12181E')
    scl.pack()
    
    lbl = tkinter.Label(text='',fg='cyan',bg="#12181E")
    lbl.pack()
    
    lbl.configure(text="")
    
    btn = tkinter.Button(myapp,width=12,text="Generate",font=('',10,'bold'),height=(2),command=gen,bg="#51E79D",fg="white")
    btn.pack(pady=20)
    
    
    ent.bind('<Double-Button-1>',copy)
    lbl.configure(text='')
    
    myapp.mainloop()


def gen ():
    lbl.configure(text='')
    ent.delete(0,END)
    sum = random.choices(all,k=scl.get())
    password = ''
    for i in sum :
        password+= i
    ent.insert(0,password)
    print(password)

def copy(x):
    
    inp = ent.get()
    ent.clipboard_clear()
    ent.clipboard_append(inp)
    lbl.configure(text="Copied!")
    lbl.after(1600,t)

def t():
    lbl.configure(text='')
    


myappUi()

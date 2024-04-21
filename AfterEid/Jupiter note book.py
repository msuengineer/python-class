import tkinter
from tkinter import *
top = tkinter.Tk()
top.title("Welcome to innovate app")
top.geometry("350x200")
labl = Label(top, text="Click Here to open jupiter note book")
labl.grid(column=0, row=0)
txt = Entry(top, width=10)
txt.grid(column=1, row=0)
def click():
	labl.configure(text="Jupiter Notebook will open ! !")
btn = Button(top, text ="Click Me", command=click)
btn.grid(column=2, row=0)
top.mainloop()

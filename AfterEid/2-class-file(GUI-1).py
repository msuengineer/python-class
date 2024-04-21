##from tkinter import Tk,Label 
##r=Tk()
##r.title('My Window')
##r.geometry('500x500+400+400')
##lab1=Label(r,text='Hello World')
##lab2=Label(r,text='Hello World')
##lab3=Label(r,text='Hello World')
##lab2.pack()
##lab1.pack()
##lab2.pack()
##lab3.pack()
##
##r.mainloop()

##from tkinter import Tk, Label
##
##r = Tk()
##r.title('My Window' )
##r.geometry('500x500+400+400')
##
##lab1 = Label(r, text='Hello World' ,fg='grey',bg='blue',borderwidth=10,relief='groove')
##lab2 = Label(r, text='Hello World')
##lab3 = Label(r, text='Hello World')
##lab1.pack()
##lab2.pack()
##lab3.pack()
##
##r.mainloop()


##from tkinter import Tk,Button,Label
##
##def func():
##    l=Label(r,text='Hello!!')
##    l.pack()
##            
##r=Tk()
##r.geometry('500x500+400+400')
##b=Button(r,text='Click it!',command=func ,fg='grey',bg='blue',borderwidth=10,relief='groove')
##b.pack()
##r.mainloop()


from tkinter import Tk,Label,Button
from tkinter.messagebox import showinfo

def func():
    showinfo(message='Hello!!')

r=Tk()
r.geometry('500x500+400+400')
b=Button(r,text='Click it!',command=func,fg='grey',bg='blue',borderwidth=10,relief='groove')
b.pack()
r.mainloop()

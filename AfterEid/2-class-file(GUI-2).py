from tkinter import Tk,Label,Button,Entry
def converter():
    fah=int(e.get())*9/5+32
    l=Label(r,text='Temperature in Fahrenheit is '+str(fah))
    l.pack()
r=Tk()
r.geometry('500x500+400+400')
r.title('Converter')
l=Label(r,text='Enter temperature in Celsius:')
l.pack()
e=Entry(r)
e.pack()
b=Button(r,text='Convert to Fahrenheit',command=converter ,fg='grey',bg='blue',borderwidth=10,relief='groove')
b.pack()
r.mainloop()

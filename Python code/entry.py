from tkinter import messagebox
from tkinter import *
top=Tk()
top.geometry("300x150")
top['bg']="green"
def add():
    f=firstNum.get()
    s=secondNum.get()
    messagebox.showinfo("sum",(f+s))
firstNum=IntVar()
secondNum=IntVar()
Label(top,text="first number",width="13").place(x=50,y=50)
Label(top,text="second number",width="13").place(x=50,y=90)
Entry(top,textvariable=firstNum).place(x=150,y=50)
Entry(top,textvariable=secondNum).place(x=150,y=90)
Button(top,text="Add",width="5",bg="orange",command=add).place(x=100,y=120)
top.mainloop()
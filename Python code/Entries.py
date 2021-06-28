from tkinter import *
top=Tk()
top.geometry("300x250")
top['bg']="#51E1DC"
label=Label(top,text="first number").place(x=50,y=50)
ent=Entry(top).place(x=150,y=50)
top.mainloop()
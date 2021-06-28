from tkinter import messagebox
from tkinter import *
top=Tk()
top.geometry("300x250")
top['bg']="#51E1DC"
def myfun():
    messagebox.showinfo("Title","you clicked on button")
btn=Button(top,text="click me",command=myfun).pack()
top.mainloop()
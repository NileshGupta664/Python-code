from tkinter import *
top=Tk()
top.geometry("300x250")
top['bg']="#51E1DC"
mb=Menubutton(top,text="programming",bg="navy",fg="white",relief=GROOVE)
mb.grid()
mb.menu=Menu(mb)
mb["menu"]=mb.menu
mb.menu.add_checkbutton(label="C")
mb.menu.add_checkbutton(label="C++")
mb.menu.add_checkbutton(label="Python")
mb.menu.add_checkbutton(label="java")
mb.pack()
top.mainloop()
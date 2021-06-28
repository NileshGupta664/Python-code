from tkinter import *
top=Tk()
top.geometry("300x150")
top['bg']="red"
Checkbutton(top,text="Apple",width="15",onvalue=1,offvalue=0).place(x=10,y=20)
Checkbutton(top,text="Mango",width="15",onvalue=1,offvalue=0).place(x=10,y=50)
Checkbutton(top,text="banana",width="15",onvalue=1,offvalue=0).place(x=10,y=80)
top.mainloop()
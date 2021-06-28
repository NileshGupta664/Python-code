from tkinter import *
top=Tk()
top.geometry("300x150")
top['bg']="red"
Label(top,text="my favoriate fruits").pack()
listbox=Listbox(top,height="20")
listbox.insert(1,"apple")
listbox.insert(2,"mango")
listbox.insert(3,"banana")
listbox.pack(pady=4)
top.mainloop()
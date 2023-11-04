from tkinter import *

root =Tk()

root.title("test")
root.geometry('200x100')

lbl=Label(root,text='hi')
lbl.grid()

def clickede():
    res = "You wrote" + txt.get()
    lbl.configure(text = res)
 
# button widget with red color text
# inside
txt = Entry(root, width=10)
txt.grid(column =1, row =0)
btn = Button(root, text = "Click me" ,
             fg = "red", command=clickede)
# set Button grid
btn.grid(column=3, row=5)

root.mainloop()
from tkinter import * 
from tkinter import messagebox

root=Tk()

root.title("Study for exam")

root.geometry('500x500')

    
lbl = Label (root,text="Hello",foreground="yellow")
lbl.grid() # grids of x,y 


input = Entry(root,width=10)
input.grid(column=2,row=0)
var=StringVar()
n=IntVar()

def tkmessagebox() :
    messagebox.showinfo("title of box", "u choose option 1 ")
    top3=Toplevel(root)
    lbl3=Label(top3,textvariable=var)
    lbl3.pack()



def open_Toplevel2():
    top2 = Toplevel(root) 
    top2.title("Toplevel1")
    top2.geometry("500x500")
    R1 = Radiobutton(top2, text="Option 1", variable=var, value="the value u get from chosing option 1 , var will store this value ",command=tkmessagebox)
    R1.pack()


def clicked():
    res = "You wrote" + input.get()
    lbl.configure(text = res)
    lbl2=Label(root,text="after clicking with font modification",font = ("arial", 60, "bold"))
    lbl2.grid(row=3)

    top1 = Toplevel(root)
    top1.title("Toplevel1")
    top1.geometry("500x500")
    label = Label(top1,text = "This is a Toplevel1 window")
    label.grid()
    button1 = Button(top1, text = "Exit",command = top1.destroy)
    button1.grid(row=3,column=2)

    button2 = Button(top1, text = "open toplevel2",fg="red",command = open_Toplevel2)
    button2.grid(row=4)




btn1 = Button(root,text = "Click me",command=clicked)
btn1.grid(column=3, row=5)

txt = Entry(root, width=10)
txt.grid(column =1, row =0)

root.mainloop()
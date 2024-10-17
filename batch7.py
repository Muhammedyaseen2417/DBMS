import tkinter

win=tkinter.Tk()
win.title("Wellcome")
win.configure(bg="gold")
win.minsize(400,400)
win.maxsize(500,500)
def save():
    print(e1.get())
    l3.config(text=e1.get())

l1=tkinter.Label(win,text="wellcome to all",bg="gold",fg="red")
l1.place(x=150,y=20)

l2=tkinter.Label(win,text="name")
l2.place(x=75,y=50)

e1=tkinter.Entry(win)
e1.place(x=150,y=50)

btn1=tkinter.Button(win,text="save",bg="white",activebackground="black",activeforeground="white",command=save)
btn1.place(x=150,y=70)

l3=tkinter.Label(win)
l3.place(x=150,y=120)


win.mainloop()
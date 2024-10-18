import tkinter
import sqlite3
# con=sqlite3.connect("tkinter_data.db")
# con.execute("create table sample(uname text,password text)")
win=tkinter.Tk()
win.title('login')
win.configure(bg="red")
win.minsize(400,400)
win.maxsize(500,500)



def reg_form():
    win1=tkinter.Tk()
    win1.title('register')
    win1.configure(bg="gold")
    win1.minsize(400,400)
    win1.maxsize(500,500)

    def reg():
        con=sqlite3.connect("tkinter_data.db")
        con.execute("insert into sample(uname,password)values(?,?)",(e3.get(),e4.get()))
        con.commit()
        win1.destroy()

    l3=tkinter.Label(win1,text="register",bg='gold',fg="black")
    l3.place(x=150,y=20)
    l5=tkinter.Label(win1,text="Fullname")
    
    l5.place(x=75,y=50)
    l6=tkinter.Label(win1,text="Address")
    l6.place(x=75,y=75)
    e3=tkinter.Entry(win1)
    e3.place(x=150,y=50)
    e4=tkinter.Entry(win1)
    e4.place(x=150,y=80)

    
    
    


    btn3=tkinter.Button(win1,text="Submmit",bg="gray",activebackground='red',activeforeground='black',padx=10,pady=8,command=reg)
    btn3.place(x=200,y=120)
    win1.mainloop()


   


l1=tkinter.Label(win,text="Login",bg='green',fg="black")
l1.place(x=150,y=20)

l2=tkinter.Label(win,text="username")
l2.place(x=75,y=50)
l4=tkinter.Label(win,text="password")
l4.place(x=75,y=75)

e1=tkinter.Entry(win)
e1.place(x=150,y=50)

e2=tkinter.Entry(win)
e2.place(x=150,y=80)



btn1=tkinter.Button(win,text="login",bg="gray",activebackground='red',activeforeground='black',padx=10,pady=8,command="save")
btn1.place(x=200,y=120)

btn2=tkinter.Button(win,text="Register",bg="gray",activebackground='red',activeforeground='black',padx=10,pady=8,command=reg_form)
btn2.place(x=200,y=300)





win.mainloop()
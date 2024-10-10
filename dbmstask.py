import sqlite3
con = sqlite3.connect("abc.db")
try:
    con.execute("create table student(roll_no int,name text,age int)")
except:
    pass

a=int(input("No of Students : "))
for i in range(a):
    roll_no=i+1
    name=input("Enter the Name : ")
    age=int(input(" Enter the age : "))

    con.execute("insert into student(roll_no,name,age)values(?,?,?)",(roll_no,name,age))
    con.commit()
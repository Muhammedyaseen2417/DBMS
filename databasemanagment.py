import sqlite3
con = sqlite3.connect("std.db")
try:
    con.execute("create table student(roll_no int,name text,age int)")
except:
    pass
# con.execute("insert into student(roll_no,name,age)values(1,'akil',18),(2,'fayas',19)")
# con.commit()

# roll=int(input("Enter the Roll_Num : "))
# name=str(input("Enter the Name : "))
# age=int(input("Enter the Age : "))
# con.execute("insert into student(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()

# data=con.execute('select age,name from student')
# for i in data:                                                                   display
#     print(i)

# name=input("enter old name : ")
# name1=input("enter new name : ")
# con.execute("update student set name=? where name=?",(name1,name))               update
# con.commit()

# roll_no=int(input("Enter the Roll-Number of Student : "))
# con.execute("delete from student where roll_no=?",(roll_no,))                    delete
# con.commit()

# data=con.execute("select * from student where name  like  '_a%' " )             
# for i in data:
#     print(i)

# data=con.execute("select * from student order by name")                       accenting order
# for i in data:
#     print(i)

# data=con.execute("select * from student order by name desc")                  decenting order
# for i in data:
#     print(i)
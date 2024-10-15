import mysql.connector

con=mysql.connector.connect(user="yaseen",host="localhost",password="Yaseen@2417",database="mysql1")
con.autocommit=True
cur=con.cursor()
# cur.execute("create database mysql1")
try:
    cur.execute("create table std (roll_num int,name text,age int)")
except:
    pass
a=int(input('Enter the No of Students'))
for i in range(a):
    roll_num=int(input("Enter the roll_number : "))
    name=input('Enter the name : ')
    age=int(input("Enter the age: "))
    cur.execute("insert into std (roll_num,name,age)values(%s,%s,%s)",(roll_num,name,age))
        




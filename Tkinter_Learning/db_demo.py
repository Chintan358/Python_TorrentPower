from tkinter import *
import mysql.connector
tops = Tk();
tops.geometry("500x500")

con = mysql.connector.connect(

        host="localhost",
        user="root",
        password="",
        port=3306,
        database="rahul"
)

def addUser():
   cursor = con.cursor()
   qry = "insert into user(uname,email,phone)values(%s,%s,%s)"
   val = (e1.get(),e2.get(),e3.get())
   cursor.execute(qry,val)
   con.commit()
   print("data inserted !!!")
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)

title = Label(tops,text="Registration",font=("Georgia",20,"bold"),fg="white",bg="black").place(x=100,y=50)

l1 = Label(tops,text="Username").place(x=100,y=100)
l2 = Label(tops,text="Email").place(x=100,y=150)
l3 = Label(tops,text="Phone").place(x=100,y=200)

e1 = Entry(tops,bg="red",fg="white")
e1.place(x=180,y=100)
e2 = Entry(tops)
e2.place(x=180,y=150)
e3 = Entry(tops)
e3.place(x=180,y=200)

b1 = Button(tops,text="Submit",width=30,command=lambda:addUser()).place(x=100,y=250)

tops.mainloop()
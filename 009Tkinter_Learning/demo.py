from tkinter import *

tops = Tk();
tops.geometry("500x500")

##########pack#######
# b1 = Button(tops,text="Left").pack(side=LEFT)
# b2 = Button(tops,text="Right").pack(side=RIGHT)
# b3 = Button(tops,text="Top").pack(side=TOP)
# b4 = Button(tops,text="Bottom").pack(side=BOTTOM)
# b5 = Button(tops,text="Center").pack(side=CENTER)

########Grid######

# l1 = Label(tops,text="Username").grid(row=1,column=1)
# l2 = Label(tops,text="Email").grid(row=2,column=1)
# l3 = Label(tops,text="Phone").grid(row=3,column=1)

# e1 = Entry(tops).grid(row=1,column=2)
# e2 = Entry(tops).grid(row=2,column=2)
# e3 = Entry(tops).grid(row=3,column=2)

# b1 = Button(tops,text="Submit").grid(row=4,column=2)


#######place#####
title = Label(tops,text="Registration",font=("Georgia",20,"bold"),fg="white",bg="black").place(x=100,y=50)

l1 = Label(tops,text="Username").place(x=100,y=100)
l2 = Label(tops,text="Email").place(x=100,y=150)
l3 = Label(tops,text="Phone").place(x=100,y=200)

e1 = Entry(tops,bg="red",fg="white").place(x=180,y=100)
e2 = Entry(tops).place(x=180,y=150)
e3 = Entry(tops).place(x=180,y=200)

b1 = Button(tops,text="Submit",width=30).place(x=100,y=250)

tops.mainloop()
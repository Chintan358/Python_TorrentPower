import sqlite3

con = sqlite3.connect("mydb.db")

# con.execute("create table student(id int primary key, name varchar(20), email varchar(50))")

# con.execute("insert into student(id,name,email) values(2,'Rahul','rahul@gmial.com')")
# con.commit()

# con.execute("update student set name='rahul-update' where id=2")
# con.commit()

# con.execute("delete from student where id=2")
# con.commit()

data = con.execute("select * from student").fetchall()
 
print(data)
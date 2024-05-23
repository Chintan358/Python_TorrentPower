import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
cursor = conn.cursor()

# qry = "insert into emp(id,uname,email,pass)values(%s,%s,%s,%s)"
# val = ('0','rahul','rahul@gmial.com','r123')
qry = "insert into emp(id,uname,email,pass)values('0','krunal','krunal@gmial.com','krunal123')"

cursor.execute(qry)
conn.commit()

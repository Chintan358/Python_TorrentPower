import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
cursor = conn.cursor()


qry = "update emp set pass=%s where id=%s"
val = ("raj123",2)

cursor.execute(qry,val)
conn.commit()

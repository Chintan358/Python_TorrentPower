import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
cursor = conn.cursor()


qry = "delete from emp where id='1'"

cursor.execute(qry)
conn.commit()

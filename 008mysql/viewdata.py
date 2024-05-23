import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
cursor = conn.cursor()


cursor.execute("select * from emp");

data = cursor.fetchall()

for i in data:
    print(i)

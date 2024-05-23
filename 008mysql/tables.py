import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)
cursor = conn.cursor()

cursor.execute("show tables")
data = cursor.fetchall()

for i in data:
    print(i)
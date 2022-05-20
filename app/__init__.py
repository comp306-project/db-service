import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="user",
  password="password",
)

cursor = mydb.cursor()
cursor.execute("USE world")
import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="user",
  password="password",
  auth_plugin='mysql_native_password',
)

cursor = mydb.cursor()
cursor.execute("USE formula")
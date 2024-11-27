import mysql.connector

connection = mysql.connector.connect (
    host='',
    user='',
    password='',
    # auth_plugin="mysql_native_password"
)

cursor = connection.cursor(buffered=True)

cursor.execute("show databases")

for i in cursor:
    print(i)

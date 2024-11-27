# MYSQL CONNECTION

~ open
`cmd`

~ type (recommended)
```bash
pip install mysql-connector-python
```

~ type
```bash
pip install mysql.connector
```

~ import library
```bash
import mysql.connector
```

~ create connection
```bash
connection = mysql.connector.connect(
 host='localhost',
 user='your_username',
 password='your_password',
 database='your_database',
 # auth_plugin='mysql_native_password'  # use when facing issues with mysql server
)
```

~ use when facing issues with mysql server<br>
~ open mysql command line client
```bash
ALTER USER 'your_username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password'
```

~ create cursor
```bash
cursor = connection.cursor()
```

~ execute query
```bash
cursor.execute(
'''
 CREATE TABLE IF NOT EXISTS user (
 id INT PRIMARY KEY,
 name VARCHAR(10)
 )
'''
)

```

~ insert data
```bash
cursor.execute(
"INSERT INTO user (id, name) VALUES (%s, %s)", (101, 'Alice'))
```

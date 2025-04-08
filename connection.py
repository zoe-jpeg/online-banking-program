"""import mysql.connector

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('SELECT * FROM student')
print(c.fetchall())
conn.close()"""

import os
import mysql.connector

def show_all():
    os.system("clear")

    connection = mysql.connector.connect(user = "root", database = "example", password = "Zb01101944!?*")

    cursor = connection.cursor()

    testQuery = ('SELECT * FROM student')

    cursor.execute(testQuery)

    for item in cursor:

        print(item)

    cursor.close()

    connection.close()

show_all()
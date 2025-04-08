import mysql.connector
import os

def show_all():
    os.system("clear")

    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host if not localhost
        user="root",       # Replace with your MySQL username
        password="Zb01101944!?*",  # Replace with your MySQL password
        database="example" # Replace with your MySQL database name
    )

    cursor = connection.cursor()

    # Query to fetch all rows from the 'student' table
    testQuery = 'SELECT * FROM student'

    cursor.execute(testQuery)

    # Print each row from the result
    for item in cursor:
        print(item)

    # Close the cursor and connection
    cursor.close()
    connection.close()

# Call the function to display all rows
show_all()
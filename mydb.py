import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Herman_02282003'
)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("Done")

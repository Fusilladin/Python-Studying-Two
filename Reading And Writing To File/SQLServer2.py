import pyodbc
import os

driver = os.environ['DB_DRVR']
server = os.environ['DB_SRVR']
database = "BOOKSTORE"
username = os.environ['DB_USER']
password = os.environ['DB_PASS']
# password = input("Password: ")
# os.system("cls")

conn = pyodbc.connect("DRIVER=" + driver
                      + ";SERVER=" + server
                      + ";DATABASE=" + database
                       + ";UID=" + username
                       + ";PWD=" + password

)

cursor = conn.cursor()

# for row in cursor.execute("select BookId, Title, Author, Category FROM BOOK"):
#     print(row.BookId, row.Title, row.Author, row.Category)

cursor.execute('SELECT * FROM BOOK')
rows = cursor.fetchall()
for row in rows:
    print(row)


















#

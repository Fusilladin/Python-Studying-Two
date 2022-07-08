import pyodbc
# from databases import Database
import pandas as pd

df = pd.read_csv('CxnnStr.txt')

ConnectionString = df 

conn = pyodbc.connect(ConnectionString)

cursor = conn.cursor()

for row in cursor.execute("select BookId, Title, Author, Category FROM BOOK"):
    print(row.BookId, row.Title, row.Author, row.Category)




import pyodbc
import pandas as pd


driver = "{SQL Server Native Client 11.0}"
server = "127.0.0.1"
database = "BOOKSTORE"
username = "Azure1"
password = "Pass1"

conn = pyodbc.connect("DRIVER=" + driver
                      + ";SERVER=" + server
                      + ";DATABASE=" + database
                       + ";UID=" + username
                       + ";PWD=" + password

)

cursor = conn.cursor()
sql_query=pd.read_sql_query('SELECT * FROM [BOOKSTORE].[dbo].[BOOK]', conn)
sql_query.to_csv('all_data.csv', index=False)
print(sql_query)










#
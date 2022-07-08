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

result = pd.read_sql('SELECT * FROM [BOOKSTORE].[dbo].[BOOK]', conn)
df = pd.DataFrame(result)
df.to_excel("FileExample.xlsx", sheet_name='Results')
# print(df)











#
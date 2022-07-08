import pyodbc

print(pyodbc.drivers())

 # [
 #    'SQL Server',
 #    'SQL Server Native Client 11.0',
 #    'ODBC Driver 17 for SQL Server',
 #    'SQL Server Native Client RDA 11.0',
 #    'Microsoft Access Driver (*.mdb, *.accdb)',
 #    'Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)',
 #    'Microsoft Access Text Driver (*.txt, *.csv)'
 #    ]

conx_string = r"driver={SQL SERVER}; server=810J9UH\userTK427; database=AdventureWorks2017; trusted_connection=YES;"
query = "SELECT Name, CreditRating FROM Purchasing.Vendor WHERE CreditRating < 3"

# conx_string = pyodbc.connect(conx_string);
# cursor = conx.cursor();
# cursor = execute(query);
# data = cursor.fetchall()
# print(data)
# conx.close()

with pyodbc.connect(conx_string) as conx:
    cursor = conx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
print(data)

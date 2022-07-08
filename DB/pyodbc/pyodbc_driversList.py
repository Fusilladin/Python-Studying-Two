import pyodbc
import pandas as pd

print("List of ODBC Drivers:\n'{}'")
dlist = pyodbc.drivers()
for drvr in dlist:
	print(drvr)
print("'{}'\nEnd of List")
 









#
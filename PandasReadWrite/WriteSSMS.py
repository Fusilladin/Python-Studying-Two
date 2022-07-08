import pypyodbc as odbc

DRIVER_NAME = 'SQL Native Client 11.0'
SERVER_NAME = 'DESKTOP-81OJ9UH'
DATABASE_NAME = 'API1'

# uid=DESKTOP-81OJ9UH\userTK427;
# pwd=<password>;
connection_string = f"""
	DRIVER={{{{DRIVER_NAME}}}};
	SERVER={SERVER_NAME};
	DATABASE={DATABASE_NAME};
	Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
print(conn)














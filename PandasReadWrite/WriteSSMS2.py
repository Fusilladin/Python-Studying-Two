import pyodbc

def read(conn):
	print("Read")
	cursor = conn.cursor()
	cursor.execute("select * from dbo.Test1")
	for row in cursor:
		print(f'row = {row}')
	print()

def create(conn):
	print("Create")
	cursor = conn.cursor()
	cursor.execute(
		'insert into dbo.Test1(a,b) values(?,?);',
		(1, 'John')
	)
	conn.commit()
	read(conn)

conn = pyodbc.connect(
	"Driver={SQL Server Native Client 11.0};"
	"Server=DESKTOP-81OJ9UH;"
	"Database=API1;"
	"Trusted_Connection=yes"
)

read(conn)
create(conn)
# update(conn)
# delete(conn)

# conn.close()













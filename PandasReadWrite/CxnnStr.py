def GetConnectionString():
    driver = "{SQL Server Native Client 11.0}"
    server = "127.0.0.1"
    database = "BOOKSTORE"
    username = "Azure1"
    password = "Pass1"

    connectionString = (
        "DRIVER=" + driver 
        + ";SERVER=" + server 
        + ";DATABASE=" + database 
        + ";UID=" + username 
        + ";PWD=" + password
        )
    return connectionString
# Using MySQL
# import CreateConnection

# def CreateDatabse():
#     CreateConnection.cursor.execute("CREATE DATABASE CareNow")

# CreateDatabse()

# Using PostgreSQL
import CreateConnection

def CreateDatabse():
    CreateConnection.cursor.execute("CREATE DATABASE Care")
    CreateConnection.db.commit
CreateDatabse()
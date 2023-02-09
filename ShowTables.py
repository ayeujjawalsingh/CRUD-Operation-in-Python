import CreateConnection

def ShowTables():
    CreateConnection.cursor.execute("SHOW TABLES")
    for x in CreateConnection.cursor:
        print(x)

ShowTables()
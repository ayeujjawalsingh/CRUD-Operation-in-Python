import CreateConnection

def ShowTables():
    CreateConnection.cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    for x in CreateConnection.cursor:
        print(x)

ShowTables()
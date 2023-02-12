import CreateConnection

def ShowDatabses():
    CreateConnection.cursor.execute("SELECT datname FROM pg_database;")
    # printing all the databases
    for i in CreateConnection.cursor:
        print(i)

ShowDatabses()
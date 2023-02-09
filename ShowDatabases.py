import CreateConnection

def ShowDatabses():
    CreateConnection.cursor.execute("SHOW DATABASES")
    # printing all the databases
    for i in CreateConnection.cursor:
        print(i)

ShowDatabses()
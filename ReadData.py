import CreateConnection
def read():
    row = int(input("How much number of row you want to print : "))
    Query1 = "Select Id,Name,Mobile,Email,Address,City,State,PinCode,DateOfBirth From user_details"
    # Query1 = "SELECT * FROM user_details LIMIT 30"
    # Query1 = "SELECT * FROM user_details LIMIT 10 OFFSET 15"
    # Query1 = "SELECT * FROM user_details LIMIT 15, 10"
    try:
        CreateConnection.cursor.execute(Query1)
        data = CreateConnection.cursor.fetchall()
        i = 0
        for x in data:
            if(i>=row):
                i=0
                break
            print(x)
            i=i+1
        print("Successful")
    except Exception as e: 
        print(e)

read()


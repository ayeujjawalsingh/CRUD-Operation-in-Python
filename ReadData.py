import CreateConnection
def read():
    # row = int(input("How much number of rows you want to print : "))
    # Query1 = "Select id,first_name,last_name,mobile_number,email_id,address,city,state,country,pin_code,date_of_birth From user_details Where status = 1"
    # Query1 = "SELECT id,first_name,last_name,mobile_number,email_id,address,city,state,country,pin_code,date_of_birth FROM user_details order by id LIMIT 30"
    Query1 = "SELECT id,first_name,last_name,mobile_number,email_id,address,city,state,country,pin_code,date_of_birth FROM user_details Where status = 1 order by id LIMIT 5 OFFSET 0 "
    # Query1 = "SELECT id,first_name,last_name,mobile_number,email_id,address,city,state,country,pin_code,date_of_birth FROM user_details LIMIT 15, 10"
    try:
        CreateConnection.cursor.execute(Query1)
        data = CreateConnection.cursor.fetchall()
        # i = 0
        for x in data:
            # if(i>=row):
            #     i=0
            #     break
            print(x)
            # i=i+1
        print("Successful")
    except Exception as e: 
        print(e)

read()


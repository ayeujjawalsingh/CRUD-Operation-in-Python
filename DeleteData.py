import CreateConnection

def delete():
    ch  = input("Enter Your Email : ")
    query2 = "UPDATE user_details SET status = 2 WHERE email_id = '{}';".format(ch)
    try:
        CreateConnection.cursor.execute(query2)
        CreateConnection.db.commit()
        print("Successful")
    except:
        print("Error")
delete()
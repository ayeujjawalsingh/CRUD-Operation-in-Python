import CreateConnection

def delete():
    ch  = input("Enter Your Row Id : ")
    query2 = "delete from user_details where id={}".format(ch)
    try:
        CreateConnection.cursor.execute(query2)
        CreateConnection.db.commit()
        print("Successful")
    except:
        print("Error")
delete()
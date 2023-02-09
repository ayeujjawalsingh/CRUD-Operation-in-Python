import CreateConnection
import re
def update():
    ch  = input("Enter Your Row Id : ")
    query2 = "Select * from  user_details where id={}".format(ch)
    try:
        CreateConnection.cursor.execute(query2)
        data = CreateConnection.cursor.fetchall()
        for x in data:
            Name = x[1]
            Mobile = x[2]
            Email = x[3]
            Password = x[4]
            Address = x[5]
            City = x[6]
            State = x[7]
            PinCode = x[8]
            DateOfBirth = x[9]
        
        print("Choose an Option : \n 1. User Name \n 2. Email \n 3. Password \n 4. Others")
        option1 = int(input("Enter Your Choise : "))
        
        if(option1 == 1):
            dummy = True
            fname = ""
            while(dummy):
                fname = input("Enter Your First Name : ")
                if(fname==''):
                    print("Please Write Your First Name")
                elif fname.replace(" ", "").isalpha():
                    dummy = False
                else:
                    print("First Name Invalid Please Provide Valid First Name")
            dummy = True
            lname = ""
            while(dummy):
                lname = input("Enter Your Last Name : ")
                if(lname==''):
                    print("Please Write Your Last Name")
                elif lname.replace(" ", "").isalpha():
                    dummy = False
                else:
                    print("Last Name Invalid Please Provide Valid Last Name")
        elif(option1==2):
            dummy = True
            email = ""
            while(dummy):
                email = input("Email : ")
                if(email_verification(email)):
                    dummy = False
                else:
                    print("Wrong Email Please Provide Valid Email")

        elif(option1==3):
            ans = input("Do You Want to change Your Password : (Y/N) ")
            if(ans == "Y" or ans == "y"):
                optpass = int(input("We must first confirm that you are a genuine individual \n Please select these option \n 1. Email \n 2. Mobile 3. Old Password \n Select : "))
                if(optpass == 1):
                    em = input("Enter your email : ")
                    QueryEmailPass = "Select Email From user_details"
                    try:
                        CreateConnection.cursor.execute(QueryEmailPass)
                        email_pass = CreateConnection.cursor.fetchall()
                        print(type(email_pass[1]))
                        if em in email_pass:
                            dob_pass = input("Please provide your Date Of Birth (DD/MM/YYYY) : ")
                            QueryDobPass = "SELECT DateOfBirth FROM person WHERE name = '{}';".format(em)
                            try:
                                CreateConnection.cursor.execute(QueryDobPass)
                                dobemailpass = CreateConnection.cursor.fetchall()
                                if(dob_pass == dobemailpass):
                                    pas = input("Enter New Password : ")
                                    encrypt_password = argon2_algo(pas)
                            except Exception as e:
                                print("Error")
                        else:
                            print('Please provide a validate email..')
                        
                            
                    except Exception as e:
                        print(e)
            
            
            
            
            
            
            elif(ans == 'N' | ans == 'n'):
                print("Good Habbit!! Don't Forget Your Password")







    #     print("Choose an Option \n 1.Name \n 2.Mobile \n 3.Email \n 4.Password \n 5.Address \n 6.City \n 7.State \n 8.PinCode \n 9.DateOfBirth")
    #     option = int(input("Enter Your Choise : "))
    #     if(option==1):
    #         Name = input("Enter Your Updated Name : ")
    #     elif(option==2):
    #         Mobile = input("Enter Your Updated Mobile : ")
    #     elif(option == 3):
    #         Email = input("Enter Your Updated Email : ")
    #     elif(option == 4):
    #         Password = input("Enter Your Updated Password : ")
    #     elif(option==5):
    #         Address = input("Enter Your Updated Address : ")
    #     elif(option == 6):
    #         City = input("Enter Your Updated City : ")
    #     elif(option == 7):
    #         State = input("Enter Your Updated State : ")
    #     elif(option==8):
    #         PinCode = input("Enter Your Updated PinCode : ")
    #     elif(option == 9):
    #         DateOfBirth = input("Enter Your Updated DOB (DD/MM/YYYY) : ")
    #     else:
    #         print("Wrong Input")
        
    #     Query = "Update user_details set Name = '{}',Mobile= '{}',Email= '{}',Password= '{}',Address= '{}',City= '{}',State= '{}',PinCode= '{}',DateOfBirth= '{}' where id = {}".format(Name,Mobile,Email,Password,Address,City,State,PinCode,DateOfBirth,ch)
    #     try:
    #         CreateConnection.cursor.execute(Query)
    #         CreateConnection.db.commit()
    #         print("Successful")
    #     except Exception as e:
    #         print(e)
    except Exception as e:
        print(e)









# ========================================================================================================== #

# Email Verification
def email_verification(email):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if(email==''):
        return False
    elif re.match(pat,email):
        return True
    return False

# ========================================================================================================== #

def argon2_algo(password):
    from argon2 import PasswordHasher
    ph = PasswordHasher()
    hash = ph.hash(password)
    return hash

# ==========================================================================================================








update()
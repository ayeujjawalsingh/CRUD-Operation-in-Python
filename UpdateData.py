import CreateConnection
import re
from argon2 import PasswordHasher

fname = ''
lname = ''
mobile = ''
email = ''
password = ''
address = ''
city = ''
state =''
country = ''
pincode = ''
dob = ''


def update():
    # ch  = input("Enter Your Row Id : ")
    # query2 = "Select * from  user_details where id={}".format(ch)
    try:
        # CreateConnection.cursor.execute(query2)
        # data = CreateConnection.cursor.fetchall()
        # for x in data:
        #     Name = x[1] 
        #     Mobile = x[2]
        #     Email = x[3]
        #     Password = x[4]
        #     Address = x[5]
        #     City = x[6]
        #     State = x[7]
        #     PinCode = x[8]
        #     DateOfBirth = x[9]
        
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



        elif(option1==4):
            other_option = int(input("Select from these :- \n 1.Address \n 2.City \n 3.State \n 4.Country \n 5.Pin Code \n 6.Date Of Birth \n Enter : "))
            print("First you need to login and then you able to edit your details.")
            email_login = input("Email : ").lower()
            # password_login = input("Password : ")
            login_querry = "SELECT COUNT(Email) FROM user_details WHERE email = '{}';".format(email_login)
            try:
                CreateConnection.cursor.execute(login_querry)
                data1 = CreateConnection.cursor.fetchall()
                if(data1[0][0]>0):
                    password_login = input("Password : ")
                    pass_query = "SELECT Password FROM user_details WHERE email = '{}';".format(email_login)
                    try:
                        CreateConnection.cursor.execute(pass_query)
                        data2 = CreateConnection.cursor.fetchall()
                        ph = PasswordHasher()
                        if(ph.verify(data2[0][0],password_login)):
                            if(other_option == 1):
                                address = input("Enter Your Address : ")
                            elif(other_option == 2):
                                city = input("Enter Your City : ")
                            elif(other_option == 3):
                                state = input("Enter Your State : ")
                            elif(other_option == 4):
                                country = input("Enter Your Country : ")
                            elif(other_option == 5):
                                pincode = input("Enter pincode : ")
                            elif(other_option == 6):
                                dob = input("Enter your date of birth (DD/MM/YYYY) : ")
                            else:
                                print("You select wrong option please try again!!")
                        else:
                            print("Wrong Password!")
                    except Exception as e:
                        print(e)
                    # print("good")
                else:
                    print("Wrong Email")
            except Exception as e:
                print("Error")


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
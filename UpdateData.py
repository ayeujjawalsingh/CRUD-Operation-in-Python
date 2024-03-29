import CreateConnection
import re
from argon2 import PasswordHasher
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from datetime import datetime
from datetime import date, timedelta

def update():
    print("Choose an Option : \n 1. User Name \n 2. Email \n 3. Password \n 4. Others")
    option1 = int(input("Enter Your Choise : "))
    
# Update User Name Section Complete
    
    if(option1 == 1):
        print("First you need to login and then you able to edit your Name.")
        email_login = input("Email : ").lower()
        login_querry = "SELECT COUNT(email_id) FROM user_details WHERE email_id = '{}';".format(email_login)
        try:
            CreateConnection.cursor.execute(login_querry)
            data1 = CreateConnection.cursor.fetchall()
            if(data1[0][0]>0):
                password_login = input("Password : ")
                pass_query = "SELECT password FROM user_details WHERE email_id = '{}';".format(email_login)
                try:
                    CreateConnection.cursor.execute(pass_query)
                    data2 = CreateConnection.cursor.fetchall()
                    ph = PasswordHasher()
                    if(ph.verify(data2[0][0],password_login)):
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
                        name_query = "UPDATE user_details SET first_name = '{}', last_name = '{}' WHERE email_id = '{}' AND password = '{}';".format(fname,lname,email_login,data2[0][0])
                        try:
                            CreateConnection.cursor.execute(name_query)
                            CreateConnection.db.commit()
                            print("Successful")
                        except Exception as e:
                            print("Error!!")
                    else:
                        print("Wrong Password!")
                except Exception as e:
                    print(e)
            else:
                print("Wrong Email")
        except Exception as e:
            print("Error")

# Update Email Section
 
    elif(option1==2):
        print("First you need to login and then you able to edit your Email.")
        email_login = input("Email : ").lower()
        login_querry = "SELECT COUNT(email_id) FROM user_details WHERE email_id = '{}';".format(email_login)
        try:
            CreateConnection.cursor.execute(login_querry)
            data1 = CreateConnection.cursor.fetchall()
            if(data1[0][0]>0):
                password_login = input("Password : ")
                pass_query = "SELECT password FROM user_details WHERE email_id = '{}';".format(email_login)
                try:
                    CreateConnection.cursor.execute(pass_query)
                    data2 = CreateConnection.cursor.fetchall()
                    ph = PasswordHasher()
                    if(ph.verify(data2[0][0],password_login)):
                        dummy = True
                        while(dummy):
                            email = input("Email : ")
                            if(email_verification(email)):
                                dummy = False
                            else:
                                print("Wrong Email Please Provide Valid Email")
                        email_query = "UPDATE user_details SET email_id = '{}' WHERE email_id = '{}' AND password = '{}';".format(email,email_login,data2[0][0])
                        try:
                            CreateConnection.cursor.execute(email_query)
                            CreateConnection.db.commit()
                            print("Successful")
                        except Exception as e:
                            print("Error!!")
                    else:
                        print("Wrong Password!")
                except Exception as e:
                    print(e)
            else:
                print("Wrong Email")
        except Exception as e:
            print("Error")

# Update Password Section

    elif(option1==3):
        ans = input("Do You Want to change Your Password : (Y/N) ")
        if(ans == "Y" or ans == "y"):
            option_password = int(input("We must first confirm that you are a genuine person or not, \n Please select these option \n 1. Email \n 2. Mobile \n 3. Old Password \n Enter : "))
            
            # Update Password Using Email and the DOB
            if(option_password == 1):
                print("Update Password Using Email")
                email_id = input("Email : ").lower()
                update_query_email = "SELECT COUNT(email_id) FROM user_details WHERE email_id = '{}';".format(email_id)
                try:
                    CreateConnection.cursor.execute(update_query_email)
                    email_id_data = CreateConnection.cursor.fetchall()
                    if(email_id_data[0][0]>0):
                        email_dob = input("Enter your Date of Birth (DD/MM/YYYY) : ")
                        email_dob_query = "SELECT date_of_birth FROM user_details WHERE email_id = '{}';".format(email_id)
                        try:
                            CreateConnection.cursor.execute(email_dob_query)
                            email_dob_data = CreateConnection.cursor.fetchall()
                            if(email_dob_data[0][0]==email_dob):
                                dummy = True
                                email_password1 = ''
                                while(dummy):
                                    email_password1 = input("New Password : ")
                                    email_password2 = input("Confirm Password : ")
                                    if(email_password1 == email_password2):
                                        if(email_password1==''):
                                            print("Please Write your Password")
                                            dummy = True
                                        elif(password_check(email_password1)):
                                            email_encrypt_new_password = argon2_algo(email_password1)
                                            email_pass_query = "UPDATE user_details SET password = '{}' WHERE email_id = '{}' AND date_of_birth = '{}';".format(email_encrypt_new_password,email_id,email_dob)
                                            try:
                                                CreateConnection.cursor.execute(email_pass_query)
                                                CreateConnection.db.commit()
                                                print("Successful")
                                            except Exception as e:
                                                print("Error!!")
                                            dummy = False
                                        else:
                                            dummy = True
                                    else:
                                        print("Your new password and confirm password are not same..")
                            else:
                                print("Wrong DOB!")
                        except Exception as e:
                            print(e)
                    else:
                        print("Wrong Email")
                except Exception as e:
                    print("Error")
            
            # Update Password Using Mobile Number and then DOB
            elif(option_password==2):
                print("Update Password Using Mobile Number : ")
                mobile_number = input("Mobile Number : ")
                update_query_mobile = "SELECT COUNT(mobile_number) FROM user_details WHERE mobile_number = '{}';".format(mobile_number)
                try:
                    CreateConnection.cursor.execute(update_query_mobile)
                    mobile_number_data = CreateConnection.cursor.fetchall()
                    if(mobile_number_data[0][0]>0):
                        mob_dob = input("Enter your Date of Birth (DD/MM/YYYY) : ")
                        mob_dob_query = "SELECT date_of_birth FROM user_details WHERE mobile_number = '{}';".format(mobile_number)
                        try:
                            CreateConnection.cursor.execute(mob_dob_query)
                            mob_dob_data = CreateConnection.cursor.fetchall()
                            if(mob_dob_data[0][0]==mob_dob):
                                dummy = True
                                mob_password1 = ''
                                while(dummy):
                                    mob_password1 = input("New Password : ")
                                    mob_password2 = input("Confirm Password : ")
                                    if(mob_password1 == mob_password2):
                                        if(mob_password1==''):
                                            print("Please Write your Password")
                                            dummy = True
                                        elif(password_check(mob_password1)):
                                            mob_encrypt_new_password = argon2_algo(mob_password1)
                                            mob_pass_query = "UPDATE user_details SET password = '{}' WHERE mobile_number = '{}' AND date_of_birth = '{}';".format(mob_encrypt_new_password,mobile_number_data[0][0],mob_dob)
                                            try:
                                                CreateConnection.cursor.execute(mob_pass_query)
                                                CreateConnection.db.commit()
                                                print("Successful")
                                            except Exception as e:
                                                print("Error!!")
                                            dummy = False
                                        else:
                                            dummy = True
                                    else:
                                        print("Your new password and confirm password are not same..")
                            else:
                                print("Wrong Password!")
                        except Exception as e:
                            print(e)
                    else:
                        print("Wrong Email")
                except Exception as e:
                    print("Error")
            
            #  Update Password Using Old Password
            elif(option_password==3):
                print("First you need to login : ")
                email_login = input("Email : ").lower()
                login_querry = "SELECT COUNT(email_id) FROM user_details WHERE email_id = '{}';".format(email_login)
                try:
                    CreateConnection.cursor.execute(login_querry)
                    data1 = CreateConnection.cursor.fetchall()
                    if(data1[0][0]>0):
                        password_login = input("Old Password : ")
                        pass_query = "SELECT password FROM user_details WHERE email_id = '{}';".format(email_login)
                        try:
                            CreateConnection.cursor.execute(pass_query)
                            old_password_data = CreateConnection.cursor.fetchall()
                            ph = PasswordHasher()
                            password1 = ''
                            if(ph.verify(old_password_data[0][0],password_login)):
                                dummy = True
                                while(dummy):
                                    password1 = input("New Password : ")
                                    password2 = input("Confirm Password : ")
                                    if(password1 == password2):
                                        if(password1==''):
                                            print("Please Write your Password")
                                            dummy = True
                                        elif(password_check(password1)):
                                            encrypt_new_password = argon2_algo(password1)
                                            old_password_query = "UPDATE user_details SET password = '{}' WHERE email_id = '{}' AND password = '{}';".format(encrypt_new_password,email_login,old_password_data[0][0])
                                            try:
                                                CreateConnection.cursor.execute(old_password_query)
                                                CreateConnection.db.commit()
                                                print("Successful")
                                            except Exception as e:
                                                print("Error!!")
                                            dummy = False
                                        else:
                                            dummy = True
                                    else:
                                        print("Your new password and confirm password are not same..")
                            else:
                                print("Wrong Password!")
                        except Exception as e:
                            print(e)
                    else:
                        print("Wrong Email")
                except Exception as e:
                    print("Error")
            
        elif(ans == 'N' | ans == 'n'):
            print("Good Habbit!! Don't Forget Your Password")
        else:
            print("Please choose correct option...")

# Update Others Section Complete

    elif(option1==4):
        other_option = int(input("Select from these :- \n 1.Address \n 2.City \n 3.State \n 4.Country \n 5.Pin Code \n 6.Date Of Birth \n Enter : "))
        print("First you need to login and then you able to edit your details.")
        email_login = input("Email : ").lower()
        login_querry = "SELECT COUNT(email_id) FROM user_details WHERE email_id = '{}';".format(email_login)
        try:
            CreateConnection.cursor.execute(login_querry)
            data1 = CreateConnection.cursor.fetchall()
            if(data1[0][0]>0):
                password_login = input("Password : ")
                pass_query = "SELECT password FROM user_details WHERE email_id = '{}';".format(email_login)
                try:
                    CreateConnection.cursor.execute(pass_query)
                    data2 = CreateConnection.cursor.fetchall()
                    ph = PasswordHasher()
                    if(ph.verify(data2[0][0],password_login)):
                        if(other_option == 1):
                            dummy = True
                            while(dummy):
                                address = input("Enter Your Address : ")
                                if(address==''):
                                    print("Please Write Your Address")
                                elif address.replace(" ", "").isalpha():
                                    dummy = False
                                else:
                                    print("Address Invalid Please Provide Valid Address")
                            address_query = "UPDATE user_details SET address = '{}' WHERE email_id = '{}' AND password = '{}';".format(address,email_login,data2[0][0])
                            try:
                                CreateConnection.cursor.execute(address_query)
                                CreateConnection.db.commit()
                                print("Successful")
                            except Exception as e:
                                print("Error!!")
                        elif(other_option == 2):
                            dummy = True
                            while(dummy):
                                city = input("Enter Your City : ")
                                if(city==''):
                                    print("Please Write Your City")
                                elif city.replace(" ", "").isalpha():
                                    dummy = False
                                else:
                                    print("City Invalid Please Provide Valid City")
                            city_query = "UPDATE user_details SET city = '{}' WHERE email_id = '{}' AND password = '{}';".format(city,email_login,data2[0][0])
                            try:
                                CreateConnection.cursor.execute(city_query)
                                CreateConnection.db.commit()
                                print("Successful")
                            except Exception as e:
                                print("Error!!")
                        elif(other_option == 3):
                            dummy = True
                            while(dummy):
                                state = input("Enter Your State : ")
                                if(state==''):
                                    print("Please Write Your State")
                                elif state.replace(" ", "").isalpha():
                                    dummy = False
                                else:
                                    print("State Invalid Please Provide Valid State")
                            state_query = "UPDATE user_details SET state = '{}' WHERE email_id = '{}' AND password = '{}';".format(state,email_login,data2[0][0])
                            try:
                                CreateConnection.cursor.execute(state_query)
                                CreateConnection.db.commit()
                                print("Successful")
                            except Exception as e:
                                print("Error!!")
                        elif(other_option == 4):
                            dummy = True
                            while(dummy):
                                country = input("Enter Your Country : ")
                                if(country==''):
                                    print("Please Write Your country")
                                elif country.replace(" ", "").isalpha():
                                    dummy = False
                                else:
                                    print("Country Invalid Please Provide Valid Country")
                            country_query = "UPDATE user_details SET country = '{}' WHERE email_id = '{}' AND password = '{}';".format(country,email_login,data2[0][0])
                            try:
                                CreateConnection.cursor.execute(country_query)
                                CreateConnection.db.commit()
                                print("Successful")
                            except Exception as e:
                                print("Error!!")
                        elif(other_option == 5):
                            dummy = True
                            while(dummy):
                                pin_code = input("PinCode : ")
                                if(pin_code == ""):
                                    dummy = False
                                if(pincode_verification(pin_code)):
                                    dummy = False
                                else:
                                    print("Wrong Pin Code Please Provide Valid Pin Code")
                            pincode_query = "UPDATE user_details SET pin_code = '{}' WHERE email_id = '{}' AND password = '{}';".format(pin_code,email_login,data2[0][0])
                            try:
                                CreateConnection.cursor.execute(pincode_query)
                                CreateConnection.db.commit()
                                print("Successful")
                            except Exception as e:
                                print("Error!!")

                        elif(other_option == 6):
                            dummy = True
                            while(dummy):
                                dob = input("Enter your date of birth (DD/MM/YYYY) : ")
                                if(is_valid_dob(dob)):
                                    dummy = False
                                else:
                                    print("Incorrect DOB!")
                                    dummy = True
                            dob_query = "UPDATE user_details SET date_of_birth = '{}' WHERE email_id = '{}' AND password = '{}';".format(dob,email_login,data2[0][0])
                            try:
                                CreateConnection.cursor.execute(dob_query)
                                CreateConnection.db.commit()
                                print("Successful")
                            except Exception as e:
                                print("Error!!")
                        else:
                            print("You select wrong option please try again!!")
                    else:
                        print("Wrong Password!")
                except Exception as e:
                    print(e)
            else:
                print("Wrong Email")
        except Exception as e:
            print("Error")
    else:
        print("Please choose correct option!!")
# ========================================================================================================== #

# Email Verification
def email_verification(email):
    pat = "^[a-zA-Z0-9.+]+@[a-zA-Z0-9]+\.(com|co\.in|[a-zA-Z]+)$"
    if(email==''):
        return False
    elif re.match(pat,email):
        return True
    return False

# ========================================================================================================== #

# Phone Number Verification
def mobile_verification(mobile):
    if(mobile==''):
        return False
    elif(re.match(r"^(\+91[-\s]?)?[0]?[6789]\d{9}$", mobile)):
        return True
    return False

# ========================================================================================================== #

# Pin Code Verification
def pincode_verification(pin_code):
    if(pin_code==''):
        return False
    elif(re.fullmatch("\d{4}|\d{6}", pin_code)):
        return True
    return False

# ========================================================================================================== #

# Password Hashing
def argon2_algo(password):
    from argon2 import PasswordHasher
    ph = PasswordHasher()
    hash = ph.hash(password)
    return hash

# ==========================================================================================================

# DOB Check
def is_valid_dob(dob_str):
    # convert the string to a date object
    try:
        dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
    except ValueError:
        print("Incorrect date format, should be DD/MM/YYYY")
        return False
    
    # check if the date is in the past
    if dob >= date.today():
        print("Date of birth should be in the past")
        return False
    
    # check if the date is not more than 150 years ago
    if dob <= date.today() - timedelta(days=365.25 * 150):
        print("Age should not be greater than 150 years")
        return False
    
    return True

# ==========================================================================================================

# Password Syntax Check
def password_check(password):
    # check length of password
    if len(password) < 8:
        return False

    # check if password has at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # check if password has at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # check if password has at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # check if password has at least one special character
    special_characters = "!@#$%^&*()_+-=[]{};:,.<>/?`~"
    if not any(char in special_characters for char in password):
        return False

    # if all conditions are met, return True
    return True

# ==========================================================================================================

# Call update function
update()
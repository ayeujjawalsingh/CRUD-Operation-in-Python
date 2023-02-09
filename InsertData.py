import CreateConnection
import re
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from datetime import datetime
from datetime import date, timedelta

def insert():
    
    # First Name
    dummy = True
    fname = ""
    while(dummy):
        fname = input("First Name : ")
        if(fname==''):
            print("Please Write Your First Name")
        elif fname.replace(" ", "").isalpha():
            dummy = False
        else:
            print("First Name Invalid Please Provide Valid First Name")

    # Last Name
    dummy = True
    lname = ""
    while(dummy):
        lname = input("Last Name : ")
        if(lname==''):
            print("Please Write Your Last Name")
        elif lname.replace(" ", "").isalpha():
            dummy = False
        else:
            print ("Last Name Invalid Please Provide Valid Last Name")

    # # Mobile Number
    dummy = True
    mobile = ""
    while(dummy):
        mobile = input("Mobile Number : ")
        if(mobile_verification(mobile)):
            dummy = False
        else:
            print("Wrong Mobile Number Please Provide Valid Mobile Number")
    
    # Email 
    dummy = True
    email = ""
    while(dummy):
        email = input("Email : ")
        if(email_verification(email)):
            dummy = False
        else:
            print("Wrong Email Please Provide Valid Email")
    
    # Password
    dummy = True
    password = ""
    while(dummy):
        password = input("Password : ")
        if(password==''):
            print("Please Write your Password")
            dummy = True
        elif(password_check(password)):
            encrypt_password = argon2_algo(password)
            dummy = False
        else:
            dummy = True
    
    # Address
    dummy = True
    address = ""
    while(dummy):
        address = input("Address : ")
        if(address==''):
            dummy = False
        elif address.replace(" ", "").isalpha():
            dummy = False
        else:
            print ("Address Invalid Please Provide Valid Address")

    # City
    dummy = True
    city = ""
    while(dummy):
        city = input("City : ")
        if(city==''):
            dummy = False
        elif city.replace(" ", "").isalpha():
            dummy = False
        else:
            print ("City Invalid Please Provide Valid City")
    
    # State
    dummy = True
    state = ""
    while(dummy):
        state = input("State : ")
        if(state==''):
            dummy = False
        elif state.replace(" ", "").isalpha():
            dummy = False
        else:
            print ("State Invalid Please Provide Valid State")
    
    # Country
    dummy = True
    country = ""
    while(dummy):
        country = input("Country : ")
        if(country==''):
            dummy = False
        elif country.replace(" ", "").isalpha():
            dummy = False
        else:
            print ("Country Invalid Please Provide Valid Country")
    
    # PinCode
    dummy = True
    pin_code = ""
    while(dummy):
        pin_code = input("PinCode : ")
        if(pin_code == ""):
            dummy = False
        if(pincode_verification(pin_code)):
            dummy = False
        else:
            print("Wrong Pin Code Please Provide Valid Pin Code")
    
    # DateOfBirth
    dummy = True
    dob = ""
    while(dummy):
        dob = input("Enter your date of birth in the format DD/MM/YYYY : ")
        if(is_valid_dob(dob)):
            dummy = False
        else:
            print("Incorrect DOB!")
            dummy = True
    
    # Query
    Query = "INSERT INTO user_details(Name,Mobile,Email,Password,Address,City,State,PinCode,DateOfBirth) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,mobile,email,encrypt_password,address,city,state,pin_code,dob)
    try:
        CreateConnection.cursor.execute(Query)
        CreateConnection.db.commit()
        print("Successful")
    except Exception as e:
        print(e)

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

def pincode_verification(pin_code):
    if(pin_code==''):
        return False
    elif(re.fullmatch("\d{4}|\d{6}", pin_code)):
        return True
    return False

# ========================================================================================================== #
  
def argon2_algo(password):
    from argon2 import PasswordHasher
    ph = PasswordHasher()
    hash = ph.hash(password)
    return hash

# ==========================================================================================================

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

insert()

# ==========================================================================================================

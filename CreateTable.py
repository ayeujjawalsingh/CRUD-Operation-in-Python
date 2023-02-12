
# Using MySQL
# import CreateConnection

# def CreateTable():
#     CreateConnection.cursor.execute("CREATE TABLE UserDetail(Id int Not Null AUTO_INCREMENT,Name varchar(100),Mobile varchar(10),Email varchar(100),Password varchar(100),Address varchar(100),City varchar(100),State varchar(100),PinCode varchar(6),DateOfBirth varchar(100),PRIMARY KEY(Id))")

# CreateTable()


#  Using PostgreSQL
import CreateConnection

def CreateTable():
    CreateConnection.cursor.execute("CREATE TABLE user_details(id SERIAL PRIMARY KEY,first_name VARCHAR(100) NOT NULL,last_name VARCHAR(100) NOT NULL,mobile_number varchar(15) UNIQUE,email_id varchar(100) UNIQUE,password varchar(100),address varchar(50),city varchar(50),state varchar(50),country varchar(50),pin_code varchar(10),date_of_birth varchar(10),status int DEFAULT 1)")
    CreateConnection.db.commit()
    print("Table created!!")
CreateTable()
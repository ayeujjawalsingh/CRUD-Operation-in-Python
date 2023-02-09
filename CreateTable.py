import CreateConnection

def CreateTable():
    CreateConnection.cursor.execute("CREATE TABLE UserDetail(Id int Not Null AUTO_INCREMENT,Name varchar(100),Mobile varchar(10),Email varchar(100),Password varchar(100),Address varchar(100),City varchar(100),State varchar(100),PinCode varchar(6),DateOfBirth varchar(100),PRIMARY KEY(Id))")

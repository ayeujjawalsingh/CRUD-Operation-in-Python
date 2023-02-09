# Importing module
import mysql.connector
 
# Creating connection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ujjawal@21",
    database = "CareNow" 
)
cursor = db.cursor()
# Printing the connection
print(db)
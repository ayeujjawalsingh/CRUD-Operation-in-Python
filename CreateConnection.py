#  Using MySQL

# # Importing module
# import mysql.connector
 
# # Creating connection
# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "Ujjawal@21",
#     database = "CareNow" 
# )
# cursor = db.cursor()
# # Printing the connection
# print(db)




#  Using Postgre SQL
import psycopg2
 
# Establishing the connection
db = psycopg2.connect(
    # database="CareNow",
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
)

cursor = db.cursor()
print(cursor)
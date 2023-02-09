import CreateConnection
import InsertData
import ReadData
import DeleteData
import UpdateData
def menu():
    print ("Select any option \n 1.Insert \n 2.Read \n 3.Update \n 4.Delete")
    ch=int(input("Enter your choice:"))
    if(ch == 1):
        InsertData.insert()
    elif(ch==2):
        ReadData.read()
    elif(ch==3):
        UpdateData.update()
    elif(ch == 4):
        DeleteData.delete()
    else:
        print("Wrong Input Choosen")
menu()

import mysql.connector
import pandas as pd
import fomulaModule as fml
import indexModul

HOST = "localhost"
USERNAME = "root"
PASSWORD = "your password" # If a password addted to your database, Please add 'passwd = PASSWORD' parameter to  mysql.connector.connect() function 
DATABASE = "sample_db"

is_Server_Running = True # Checking is the server running or not. If not set this to False automatically using except


# ----------- Try To Connect with DATABASE -----------
try:

    # Passing server details to mysql function and try to connect with DATABASE
    mydb = mysql.connector.connect(
        host= HOST,
        user= USERNAME,
        database=DATABASE
    )

    
    mycursor = mydb.cursor() # Assigning a cursor to Read & Write data in DATABASE

    
except:
    is_Server_Running = False # If server is not running or not connected setting False, So application wont run enymore




# ----------- Function to show all commands that can be use in this software (all commands are stored in 'allCommandsDic' dictionary) -----------
def showAllCommands():
    print(f"\n{'-'*20}") # Printing a line to separate the content

    # Iterating through the 'allCommandsDic' Dictionary
    for x in allCommandsDic:
        print(f"{x} : {allCommandsDic[x]}") # Printing values one by one

    print(f"{'-'*20}\n") # Printing a line to separate the content



# ----------- Function to get User details and add it to the 'al_students' table -----------
def getUserDetails():
    # Running a endless loop
    while True:
        # Asking to make sure want to add a value
        print("\n")# going to a new line
        inputChoice = input("Add a new row? (Y/N) :")
        print("\n")# going to a new line

        # check the user input. If yes -> process. If no -> back to getcommand()
        if inputChoice.lower() == "y" or inputChoice.lower() == "yes":
            
            # set id to a value that not exist in table ( value = last value +1 )
            id = indexModul.currentIndex()
            
            # Getting other inputs
            fname = input("Enter your first name :")
            sname = input("Enter your second name :")
            fullname = input("Enter your full name :")
            regnum = input("Enter your admission number :")
            classname = input("Enter Your class (ex 12-T) :")
            
            # Print all the entered detals 
            print(f"\n{'-'*15}\nYour Details: \nID               : {id} \nFull Name        : {fullname} \nFirst Name       : {fname} \nSecond Name      : {sname} \nAdmission Number : {regnum} \nClass            : {classname}\n{'-'*15}\n")

            # Again make sure admin wants to add this data to table
            is_sure = input("Are you want to add these details in to database? (Y/N) :")

            # check the user input. If yes -> process. If no -> back to getcommand()
            if is_sure.lower() == "yes" or is_sure.lower() == "y":
                # Adding the details to new raw in selected table 
                # addToTableFormula() function Generates the formula using formula Module
                mycursor.executemany(fml.addToTableFormula(), [(id,fname,sname,fullname,regnum,classname)])
                mydb.commit() # Commit all changes to data base. If not, data base doesn't update

                indexModul.increaseCurrentIndexByOne() # Increase current index by 1 becouse new data has added to table (New index = current index + 1)

                print("\nYour data added to the server!\n")
                

            elif is_sure.lower() == "no" or is_sure.lower() == "n":
                # If user says no, New details aren't adding to list.
                print("\nYour data not added to the server!")
                print(f"\n{'-'*20}")
                print("Back to Command Menu ->")
                print(f"{'-'*20}\n")

                # Going back to getcommand()
                getCommand()
                
            else:
                # If user input a wrong answer. Recall the getuserdetals() and bring back to beginning
                getUserDetails()

        # If user say they dont want to add a new details. calling the getCommand()
        elif inputChoice.lower() == "n" or inputChoice.lower() == "no":
            getCommand()

        # If user entered wrong input, Recall the getuserdetals() and bring back to beginning
        else:
            print("Command not clear please enter 'yes' or 'no' (Y/N)")
            print("\n")
            getUserDetails()

# ----------- Function to update a record in any database -----------
def updateDatainDB():
    # Making sure wants to update database or not
    # If want -> Continue process. If not -> Back to getCommand()
    wantToUpdateDatabase = input("Are you really want to update date in DataBase ? (Y/N) :")

    if wantToUpdateDatabase.lower() == "yes" or wantToUpdateDatabase.lower() == "y":

        #table, findColumn , findValue, changeColumn , changeValue
        print(f"\n{'-'*15} All Tables in DataBase {'-'*15}\n")
        mycursor.execute("SHOW TABLES")
        indexShowDB = 1
        for alldbs in mycursor:
            print(f"{indexShowDB} : '{alldbs[0]}'")
            indexShowDB+=1
        print("\n")# going to a new line

        tableToUpdate = input("Enter the table name what you want to update : ")
        print("\n")# going to a new line

        if tableToUpdate == "al_students" or tableToUpdate == "'al_students'":
            
            # This variable pass to the find column
            primaryKey  = "regnum"

            # getting value to find colomn value
            regnumber = input("Enter the student's admission number : ")
            print(f"'{regnumber}'(Regnum) Selected \n")


            # Show all the columns in the Table
            allColumnsInTable = ("id", "fname", "sname", "fullname", "class")
            print(f"\n{'-'*15} All columns in Table {'-'*15}\n")
            indexShowColumn = 1
            for allcolumns in allColumnsInTable:
                print(f"{indexShowColumn} : {allcolumns}")

            print("\n")# going to a new line

            updatechangeColomn = input("What is the column name you want to update? : ")
            
            # Makingsure Column name is correct. if not recalling the Update data function
            if updatechangeColomn not in allColumnsInTable:
                print(f"{'-'*15} \nWrong Coloumn name \nBack to beginning! \n{'-'*15}\n")
                updateDatainDB()
            else:
                pass

            # If column name is correct getting values to change in that column
            updatechangeValue = input("Enter your value to update (This will replace existing value) : ")

            print("\n")# going to a new line

            # Asking for confirm replacing 
            print(f"Replacing {regnumber}'s {updatechangeColomn} with {updatechangeValue}")
            replaceConformation = input("Are you sure want to update that? (Y/N) : ")

            # If comfirm -> do the changes. If not -> Back to getCommand()
            if replaceConformation.lower() == "yes" or replaceConformation.lower() == "y":
                # Generate the formula using formula Module
                updateFormula = fml.updateData(tableToUpdate,primaryKey,regnumber,updatechangeColomn,updatechangeValue)
                
                mycursor.execute(updateFormula) # execute generated formula using cursor
                mydb.commit() # commit all changes to the DataBase

                print(f"\n{'-'*20}")
                print("DataBase Updated!")
                print(f"{'-'*20}\n")
            
            else:
                print("Nothing Changed!")
                print(f"\n{'-'*20}")
                print("Back to Command Menu ->")
                print(f"{'-'*20}\n")
                getCommand()

        else:
            print("Please Enter a valid name!")
            updateDatainDB()
    else:
        print("Nothing Changed!")
        print(f"\n{'-'*20}")
        print("Back to Command Menu ->")
        print(f"{'-'*20}\n")
        getCommand()



# ----------------------------------------------------------------------------------------        

# All Command that use in this sofware
allCommandsDic = {
    "/showAllCommands" : "To view All Commands",
    "/inputData      " : "To enter data to database",
    "/updateData     " : "To Update a data in database"
}

# ----------------------------------------------------------------------------------------        



# ----------- Main Function in this sofware (Getting user's commands) -----------
def getCommand():
    print("/showAllCommands - To view all commands\n") # Show a sample command to inform the user
        
    # Running a endless loop
    while True:
        # Geting the user input
        commandToDo = input("Enter your Command >> ")

        if commandToDo.lower() == "/showallcommands":            
            showAllCommands() 
            
        elif commandToDo.lower() == "/inputdata":
            getUserDetails()

        elif commandToDo.lower() == "/updatedata":
            updateDatainDB()

        else:
            pass # Ignoring if user entered a wrong command





# ----------- RUNNING CHECK -----------

# Check if server is running or not
if is_Server_Running == True:
    getCommand() # if server is running -> getcommand()
else:
    # If server os not running print a error message!
    print("Can't Connect to server!")
    input("Press enter to Exit")

# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KBanfill,2.21.2022,Added code to complete assignment 5
# KBanfill,2.22.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # An object that represents a file
strFile = "ToDoList.txt"   # A string for our file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()    # existing data loaded into memory and text file closed

# # -- Input/Output -- #
# # Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
#     # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow)
        continue
#     # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = (input("Please enter a task: "))
        strPriority = (input("Please enter its priority: "))
        dicRow = {"Task": strTask.strip(), "Priority": strPriority.strip()}
        lstTable.append(dicRow)
        print("Task successfully added.")
        continue
#     # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("Your current tasks: " + "\n")
        for row in lstTable:
            print(row["Task"])

        strRemoveTask = input("Which task do you want to remove?: ")
        RemoveConfirm = False
        for row in lstTable:
            if row["Task"].lower() == strRemoveTask.lower():
                lstTable.remove(row)
                RemoveConfirm = True
                print("Task successfully removed.")
        if RemoveConfirm == False:
            print('Unable to find "', strRemoveTask, '".')

#     # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        print("Tasks successfully saved.")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strExitChoice = input('Are you sure you want to exit? (yes/no) ')
        if strExitChoice.lower() == "yes":
            break
        else:
            continue
    else:
        print('Please select a number between 1 and 5.')
# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Timothy McDowell, 5-17-22, Create a table of data):
# RRoot,1.1.2030,Created started script
# Timothy McDowell, 5-17-22 ,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

file = open(objFile, "r")
for row in file:
  lstRow = row.split(",")
  dicRow = {"task":lstRow[0],"priority":lstRow[1].strip()}
  lstTable.append(dicRow)
file.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    
    print(
    'Menu of Options\n',
    '1) Show current data\n',
    '2) Add a new item.\n',
    '3) Remove an existing item.\n',
    '4) Save Data to File\n',
    '5) Exit Program\n'
    )
    print()  # adding a new line for looks
    print()  # adding a new line for looks
    print()  # adding a new line for looks
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print()
            print("Entry #" + str(lstTable.index(row)), row["task"] + "," + row["priority"],"\n")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("Enter the task: ")
        priority = input("Enter the priority number: ")
        dicRow = {"task":task,"priority":priority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        item = int(input("Entry number to remvoe?: "))
        lstTable.pop(item)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        save = open(objFile, "w")
        for row in lstTable:
            save.write(row["task"] + "," + row["priority"])
            save.write("\r")
        save.close()   
        null = input("Your data has been saved, press any key to continue: ")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("goodbye")
        break  # and Exit the program

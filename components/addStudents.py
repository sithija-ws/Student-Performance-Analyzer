import sqlite3 as sql

connection = sql.connect("data/students.db")
curser = connection.cursor()

#create student table
curser.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        studentId TEXT PRIMARY KEY,
        name TEXT,
        python INTEGER,
        maths INTEGER,
        database INTEGER
    )
""")

connection.commit()

#check is mark is valid
def verifyMark(mark):
    if(mark>100 or mark <0):
        return False
    else :
        return True

def AddStudent():
    print("\nAdd Student 👤📱")
    while True:
        
        studentID = input("Student id: ")

        #check is already exists
        curser.execute("SELECT * FROM Students WHERE studentId = ?", (studentID,))
        existingStudent = curser.fetchone()

        if(existingStudent) :
            print("Student number is already registered. please try different one 😕❌")
        else :
            break

    name = input("name: ")
    print("\n--Marks--")
    
    while True:
        python = int(input("\tPyhon: "))
        if(verifyMark(python) == False):
            print("Please enter valid mark!")
        else :
            break
    while True:
        maths = int(input("\tMaths: "))
        if(verifyMark(maths) == False):
            print("Please enter valid mark!")
        else :
            break

    while True:
        database = int(input("\tDatabase: "))
        if(verifyMark(database) == False):
            print("Please enter valid mark!")
        else :
            break

    curser.execute("INSERT INTO Students (studentId, name, python, maths, database) VALUES (?,?,?,?,?)", (studentID, name, python,maths,database))
    
    curser.execute("SELECT * FROM Students WHERE studentId = ?", (studentID,))
    createdUser = curser.fetchone()

    print("Student Added Successfully...")
    print(f"New Student:\n\tStudent ID - {createdUser[0]}\n\tname = {createdUser[1]}")
    print(f"Marks:\npython\tmaths\tdatabase")
    print(f"{createdUser[2]}\t{createdUser[3]}\t{createdUser[4]}")
import sqlite3 as sql



connection = sql.connect("data/User.db")
curser = connection.cursor()

curser.execute("""
    CREATE TABLE IF NOT EXISTS User(
        username TEXT PRIMARY KEY,
        password TEXT
    )
""")

connection.commit()

def Login():
    choice = int(input("1. Register\t2. Login\nSelect choice: "))
    if choice == 1:
        while True:
            username = input("Create username: ")
            curser.execute("SELECT * FROM User where username = ?", (username,))
            existingUser = curser.fetchone()
            if(existingUser):
                print("Username is already in use! retry create a username 😕")
                continue
            else :
                while True :
                    password = input("password: ")
                    if(password==""):
                        print("password is required! retry...")
                        continue
                    else :
                        break
                curser.execute("INSERT INTO User (username,password) VALUES (?,?)", (username, password))
                connection.commit()
                print("User Account Created Successfully... Please Login to Use the Service ❤️")
                break

    #Login
    print("Login:\n")
    while True:
        username = input("Enter username (-1 to exit): ")
        if(username == "-1"):
            print("Thankyou for having us on your work ❤️... bye!")
            exit(0)
        password = input("password: ")

        #check is exists user
        curser.execute("SELECT * FROM User WHERE username = ?", (username,))
        existingUser = curser.fetchone()
        if existingUser:
            userpswd = existingUser[1]
            if(password == userpswd):
                print("Login successfully ✅")
                connection.close()
                return existingUser[0]
            else :
                print("Invalid Credentials! please retry 😕❌")
                continue
        else :
            print("Invalid Credentials! please retry 😕❌")
            continue
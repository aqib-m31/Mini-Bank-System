import mysql.connector
import time

class DB:
    def __init__(self,server,user,pwd) -> None:
        self.server = server
        self.user = user
        self.pwd = pwd
        self.con = mysql.connector.connect(host = server, username = user, password = pwd)
    
    def createDB(self):
        query = f"create database if not exists bank;"
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        c.close()
        self.con.close()
    
    def createTable(self,db):
        self.db = db
        self.con = mysql.connector.connect(host = self.server, username = self.user, password = self.pwd, database = db)
        query1 = f"create table if not exists users (Name varchar(30) unique not null, Country varchar(15) not null, Contact varchar(15) unique not null, Email varchar(30) unique not null, Password varchar(16) unique not null, AccountNo char(16) unique not null, CurrentBalance float not null, primary key(AccountNo));"
        c = self.con.cursor()
        c.execute(query1)
        self.con.commit()
        c.close()
        self.con.close()

print("Install MySQL server from https://mysql.com and set up the user account.")
try:
    inp = input("Enter 'DONE' if you've already installed MySQL server or press enter to exit: ")
    if inp.upper() == "DONE":
        #connect to localhost using username and pwd
        print("Login to connect to the server")
        username = input("\tEnter username: ")
        password = input("\tEnter password: ")
        print("Please Wait! Connecting to the server", end="")
        for i in "...":
            print(i,end="",flush=True)
            time.sleep(1)
        time.sleep(2)
        print()
        try:
            database = DB("localhost",username,password)
            print("Sucessfully connected to the server!")
            time.sleep(2)
            print("Setting up the database. Please wait", end="")
            for i in "...":
                print(i,end="",flush=True)
                time.sleep(2)
            time.sleep(1)
            print()
            database.createDB()
            database.createTable("bank")
            print("Database successfully created. You can now use Minibank System")
            for i in "Have a nice day:)":
                print(i, end="", flush=True)
                time.sleep(0.05)
            close = input()
        except:
            print("Oops! Can't connect to the server!\nPlease check the login credentials and re-run the program.")
            for i in "Have a nice day:)":
                print(i, end="", flush=True)
                time.sleep(0.05)
            print()
            close = input()
            exit()
    
    else:
        print("Install the required file from https://mysql.com and re-run the program.")
        for i in "Have a nice day:)":
            print(i, end="", flush=True)
            time.sleep(0.05)
        print()
        close = input()
        
except:
    print("Oops! an error occurred! Exiting the program.")
    for i in "Have a nice day:)":
        print(i, end="", flush=True)
        time.sleep(0.05)
    print()
    close = input()
    exit()

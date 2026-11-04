from utils.login import Login
from components.addStudents import AddStudent
import os
import numpy as np


print("Welcome to Student Performance Analyzer🔎✅")
username = Login()

print(f"\nHello {username}! Welcome back ❤️")
choice = int(input("1. Add Student\t2. View Students\t3. Search student through id\t4. exit\nchoice: "))

if(choice==1):
    AddStudent()
elif(choice==4):
    print("Thankyou for using me ❤️😲\tbyee....")
    exit(1)
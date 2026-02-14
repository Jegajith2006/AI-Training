import os

path = input("Enter directory path: ")

if os.path.exists(path):
    print("Directory Exists")
else:
    print("Directory Does Not Exist")

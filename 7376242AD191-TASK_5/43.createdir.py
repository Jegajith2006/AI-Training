import os

name = input("Enter directory name: ")

if not os.path.exists(name):
    os.mkdir(name)
    print("Directory Created")
else:
    print("Directory Already Exists")

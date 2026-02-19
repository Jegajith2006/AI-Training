import os

folder = input("Enter folder name: ")

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder Created")
else:
    print("Folder Exists")

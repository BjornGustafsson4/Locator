import os
import shutil
import glob


filename = input("What is the name of the file you're looking for: ")
extention = input("Is there a specific extention you want moved? (if no put 'Skip'): ")
sourceFolder = input("What is the source: ")
destination = input("What is the destination (put 'Create' for a new destination): ")
name = input("Name of composer (First Last,'None' to skip, 'Delete' to remove text): ")


if extention.upper() == "SKIP":
    extention = ".*"


#Makes new directory based on inputted file name
if destination == "Create":
    inSource = input("Do you want to create a new folder in the source?(y/n): ")
    if inSource.upper() == "Y":
        destination = os.path.join(sourceFolder, filename)
    else:
        destination = input("Please input a new directory: ")
    if os.path.exists(destination) == True:
        print("This destination already exists")
    else:
        os.mkdir(destination)
        print(f"A new folder was created at: {destination}")
elif destination.upper() == "SKIP":
    destination = sourceFolder


#Locates all subdirectories and searches for file
def listdirs(sourceFolder):
    for file in os.listdir(sourceFolder):
        d = os.path.join(sourceFolder, file)
        if os.path.isdir(d):
            print(d)
            listdirs(d)
            if d == destination:
                continue
            else:
                for file in glob.glob(f"{d}\{filename}*{extention}"):
                    shutil.move(file, destination)

 
listdirs(sourceFolder)


#To rename files
#TODO It works but should be cleaner
if name.upper() == "NONE":
    print(f"Done! The files have been transfired")
elif name.upper() == "DELETE":
    deleteTxt = input("What do you want to delete? ")
    for deleteFTxt in os.listdir(destination):
        newTxt = deleteFTxt.replace(deleteTxt, '')
        newTxt = f"{destination}\{newTxt}"
        oldTxt = f"{destination}\{deleteFTxt}"
        os.rename(oldTxt, newTxt)
    print(f"Done! {deleteTxt} has been removed from {destination}")
else:
    firstName, lastName = name.split(" ")
    for filenames in os.listdir(destination):
        oldName = f"{destination}\{filenames}"
        newName = f"{destination}\{lastName}, {firstName} {filenames}"
        os.rename(oldName, newName)
    print(f"Done! The files have been transfired and renamed to: {os.listdir(destination)}")
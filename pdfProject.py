import os
import shutil
import glob
import sys


def fileFormat(extention):
    if extention.upper() == "SKIP" or " ":
        extention = ".*"


#Makes new directory based on inputted file name
def destinationMake(destination):
    if destination.upper() == "CREATE":
        inSource = input("Do you want to create a new folder in the source?(y/n): ")
        if inSource.upper() == "Y":
            destination = os.path.join(sourceFolder, filename)
        else:
            destination = input("Please input a new directory: ")
        if os.path.exists(destination) == True:
            print("This destination already exists")
            return destination
        else:
            os.mkdir(destination)
            return destination
    elif destination.upper() == "SKIP":
        destination = sourceFolder


#Locates all subdirectories and moves files
def listdirs(sourceFolder):
    for file in os.listdir(sourceFolder):
        d = os.path.join(sourceFolder, file)
        if os.path.isdir(d):
            print(d)
            listdirs(d)
            if d == destinationNew:
                continue
            else:
                for file in glob.glob(f"{d}\{filename}*{extention}"):
                    shutil.move(file, destinationNew)


def nameFile(name):
    if name.upper() == "DELETE":
        deleteTxt = input("What do you want to delete? ")
        for deleteFTxt in os.listdir(destinationNew):
            newTxt = deleteFTxt.replace(deleteTxt, '')
            newTxt = f"{destinationNew}\{newTxt}"
            oldTxt = f"{destinationNew}\{deleteFTxt}"
            os.rename(oldTxt, newTxt)
        print(f"Done! {deleteTxt} has been removed from files in {destinationNew}")
    else:
        firstName, lastName = name.split(" ")
        for filenames in os.listdir(destinationNew):
            oldName = f"{destinationNew}\{filenames}"
            newName = f"{destinationNew}\{lastName}, {firstName} {filenames}"
            os.rename(oldName, newName)
        print(f"Done! The files have been transfired and renamed to: {os.listdir(destinationNew)}")        


print("What would you like to do: \n 1. Move files \n 2. Rename files \n 3. Move and rename files \n 4. Quit")
select = input("> ")
if select == "1":
    filename = input("What is the name of the file you're looking for: ")
    extention = input("Is there a specific extention you want moved? (if no put 'Skip'): ")
    sourceFolder = input("What is the source: ")
    destination = input("What is the destination (put 'Create' for a new destination): ")
    fileFormat(extention)
    destinationNew = destinationMake(destination)
    listdirs(sourceFolder)
elif select == "2":
    filename = input("What is the name of the file you're looking for: ")
    extention = input("Is there a specific extention you want moved? (if no put 'Skip'): ")
    destinationNew = input("What is the source for the file: ")
    name = input("Name of composer (First Last, 'Delete' to remove text): ")
    nameFile(name)
elif select == "3":
    filename = input("What is the name of the file you're looking for: ")
    extention = input("Is there a specific extention you want moved? (if no put 'Skip'): ")
    sourceFolder = input("What is the source: ")
    destination = input("What is the destination (put 'Create' for a new destination): ")
    name = input("Name of composer (First Last, 'Delete' to remove text): ")
    fileFormat(extention)
    destinationNew = destinationMake(destination)
    listdirs(sourceFolder)
    nameFile(name)
elif select == "4":
    sys.exit()
else:
    print("Please use one of the numbers to select an option")
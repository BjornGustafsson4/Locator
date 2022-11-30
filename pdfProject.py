import os
import shutil
import glob
import sys


#Checks file extention
def fileFormat(extention):
    if extention.upper() == "SKIP":
        extention = ".*"
    elif extention[0] != ".":
        extention = "." + extention
    return extention


#Makes new directory based on inputted file name
def destinationMake(destination, sourceFolder, filename):
    if destination.upper() == "CREATE":
        inSource = input("Do you want to create a new folder in the source?(y/n): ")
        if inSource.upper() == "Y":
            destination = os.path.join(sourceFolder, filename)
        else:
            destination = input("Please input a new directory: ")
        if os.path.exists(destination) == True:
            print("This destination already exists")
        else:
            os.mkdir(destination)
    elif destination.upper() == "SKIP":
        destination = sourceFolder
    return destination


#moves files from the directory and all subdirectories recursivly
def listdirs(sourceFolder, filename, extention, destinationNew):
    for folder in glob.glob(f"{sourceFolder}\**", recursive=True):
        if folder == destinationNew:
            continue
        else:
            for file in glob.glob(f"{folder}\{filename}*{extention}"):
                shutil.move(file, destinationNew)


#For renaming files and deleting text from files
def nameFile(name, destinationNew):
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
        newName = f"{destinationNew}\{lastName}, {firstName} {filenames}"
        for filenames in os.listdir(destinationNew):
            oldName = f"{destinationNew}\{filenames}"
            newName = f"{destinationNew}\{lastName}, {firstName} {filenames}"
            os.rename(oldName, newName)
        print(f"Done! The files have been transfired and renamed to: {os.listdir(destinationNew)}")


#For selecting what functions to be run
print("What would you like to do: \n 1. Move files \n 2. Rename files \n 3. Move and rename files \n 4. Quit")
select = input("> ")
if select == "1":
    filename = input("What is the name of the file you're looking for: ")
    extention = input("Is there a specific extention you want moved? (if not put 'Skip'): ")
    sourceFolder = input("What is the source: ")
    destination = input("What is the destination (put 'Create' for a new destination): ")
    extention = fileFormat(extention)
    destinationNew = destinationMake(destination, sourceFolder, filename)
    listdirs(sourceFolder, filename, extention, destinationNew)
elif select == "2":
    filename = input("What is the name of the file you're looking for: ")
    extention = input("Is there a specific extention you want moved? (if not put 'Skip'): ")
    destinationNew = input("What is the source: ")
    name = input("Name of composer (First Last, 'Delete' to remove text): ")
    nameFile(name, destinationNew)
elif select == "3":
    filename = input("What is the name of the file you're looking for: ")
    extention = input("Is there a specific extention you want moved? (if no put 'Skip'): ")
    sourceFolder = input("What is the source: ")
    destination = input("What is the destination (put 'Create' for a new destination): ")
    name = input("Name of composer (First Last, 'Delete' to remove text): ")
    extention = fileFormat(extention)
    destinationNew = destinationMake(destination, sourceFolder, filename)
    listdirs(sourceFolder, filename, extention, destinationNew)
    nameFile(name, destinationNew)
elif select == "4":
    sys.exit()
else:
    print("Please use one of the numbers to select an option")
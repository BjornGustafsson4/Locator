import os
import shutil
import glob


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
def moveFiles(sourceFolder, filename, extention, destinationNew):
    for folder in glob.glob(f"{sourceFolder}\**", recursive=True):
        if folder == destinationNew:
            continue
        else:
            for file in glob.glob(f"{folder}\*{filename}*{extention}"):
                shutil.move(file, destinationNew)


#TODO Make renaming also able to move files later
#Adds or deletes text in a file name
def namer(destinationNew, filename, extention):
    while True:
        addOrDelete = input("Do you want to 'add' or 'delete' text? ")
        textChange = input("What text do you want to add or delete? ")
        textChange = textChange.replace(" ", "_")
        textChange = textCheck(textChange)
        if addOrDelete.upper() == "ADD":  
            position = input("Do you want the new text 'before' or 'after' the file name? ")  
            if position.upper() == "AFTER":
                for file in glob.glob(f"{destinationNew}\*{filename}*{extention}"):
                    filelist = file.rsplit(".", 1)
                    fileNew = f"{filelist[0]}_{textChange}.{filelist[1]}"
                    shutil.move(file, fileNew)
                print("Done!")
                exit()
            elif position.upper() == "BEFORE":
                for file in glob.glob(f"{destinationNew}\*{filename}*{extention}"):
                    filelist = file.rsplit("\\", 1)
                    fileNew = f"{filelist[0]}\\{textChange}_{filelist[1]}"
                    shutil.move(file, fileNew)
                print("Done!")
                exit()
            else:
                print("Please use valid data.\n\n\n")
                continue
        elif addOrDelete.upper() == "DELETE":
            for file in glob.glob(f"{destinationNew}\*{filename}*{extention}"):
                filelist = file.rsplit("\\", 1)
                fileNew = f"{filelist[0]}\\{filelist[1].replace(textChange, '')}"
                shutil.move(file, fileNew)
            print("Done!")
            exit()
        else:
            print("Please use valid data.\n\n\n")
            continue


#Checks file extention for illegal characters
def fileFormat(extention):
    testlist = []
    for characters in list(extention):
        if characters.isalnum():
            testlist.append(characters)
    extention = "".join(testlist)
    if extention.upper() == "SKIP" or extention == '':
        extention = ".*"
    else:
        extention = "." + extention
    return extention


#Checks filename for illegal characters
def textCheck(filename):
    illegalCharacter = ["\\", "/", "|", ",", ":", "#", '"', "?", "<", ">", "*", " "]
    characterList = []
    for character in list(filename):
        if character not in illegalCharacter:
            characterList.append(character)
    filename = "".join(characterList)
    return filename

#For selecting what functions to be run
while True:
    print("What would you like to do: \n 1. Move files \n 2. Rename files \n 3. Move and rename files \n 4. Quit")
    select = input("> ")
    if select == "1":
        while True:
            filename = input("What is the name of the file you're looking for: ")
            extention = input("Is there a specific extention you want moved? (if not put 'Skip'): ")
            sourceFolder = input("What is the source: ")
            destination = input("What is the destination (put 'Create' for a new destination): ")
            extention = fileFormat(extention)
            filename = textCheck(filename)
            if filename == "" or extention == "" or sourceFolder == "" or destination =="":
                print("please input valid data\n\n\n")
                continue
            else:
                break
        destinationNew = destinationMake(destination, sourceFolder, filename)
        moveFiles(sourceFolder, filename, extention, destinationNew)
    elif select == "2":
        while True:
            filename = input("What is the name of the file you're looking for: ")
            extention = input("Is there a specific extention you want moved? (if not put 'Skip'): ")
            destinationNew = input("What is the source: ")
            extention = fileFormat(extention)
            filename = textCheck(filename)
            if filename == '' or extention == '' or destinationNew == '':
                print("please input valid data\n\n\n")
                continue
            else:
                break
        namer(destinationNew, filename, extention)
    elif select == "3":
        while True:
            filename = input("What is the name of the file you're looking for: ")
            extention = input("Is there a specific extention you want moved? (if no put 'Skip'): ")
            sourceFolder = input("What is the source: ")
            destination = input("What is the destination (put 'Create' for a new destination): ")
            extention = fileFormat(extention)
            filename = textCheck(filename)
            if filename == "" or extention == "" or sourceFolder == "" or destination =="":
                print("please input valid data\n\n\n")
                continue
            else:
                break
        destinationNew = destinationMake(destination, sourceFolder, filename)
        moveFiles(sourceFolder, filename, extention, destinationNew)
        namer(destinationNew, filename, extention)
    elif select == "4":
        exit()
    else:
        print("Please use one of the numbers to select an option\n\n\n")
        continue

from pathlib import Path


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate (items):
        print(f"{i+1} : {items}")



def createfile():
    try:
        readfileandfolder()
        name = input("Tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input('What you want to write in this file :- ')
                fs.write(data)
            
            print(f"FILE CREATED SUCCESSFULLY")
        
        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occured as {err}")



def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            
            print(f"READ SUCCESSFULLY")

        else:
            print("No such file exists")
    
    except Exception as err:
        print(f"An error occured as {err}")
    
    

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():

            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")

            res = int(input("Please tell your response :- "))

            
            if res == 1:
                name2 = input("Tell the new name of your file :- ")
                p2 = Path(name2)
                p.rename(p2)

                print(f"FILE NAME CHANGED SUCCESSFULLY")

            if res == 2:
                with open(p,"w") as fs:
                    data = input("What you want to write, this will overwrite the data of your file :- ")
                    fs.write(data)

                print(f"OVERWRITE SUCCESSFULLY")
                
                

            if res == 3:
                with open(p,"a") as fs:
                    data = input("What you want to add in your file :- ")
                    fs.write(" "+data)
                
                print(f"APPENDED SUCCESSFULLY")
  
    except Exception as err:
        print(f"An error occured as {err}")



def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink(p)

        print(f"FILE REMOVED SUCCESSFULLY")

    except Exception as err:
        print(f"An error occured as {err}")


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 deleting a file")

check = int(input("Please tell you response :- "))


if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()

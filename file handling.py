print("########################################")
print("#            FILE HANDELING            #")
print("########################################")
def ins():
    print("1. create new file")
    print("2. Edit or update the file")
    print("3. list the files")
    print("4. Delet the file")
    print("5. Rename the file")
    print("6. Stop the program")
ins()

c=int(input('Enter ur choice: '))

def create_file():
    name=input('Enter the file name: ')
    with open(name+".txt","w")as file:
        file.write("Welcome")
    print(name,"created sucessfully..")

match c:
    case 1:
        print("creating File")
        create_file()
    case 2:
        print("Edit")
    case 3:
        print("List file")
    case 4:
        print("Delet file")
    case 5:
        print("Rename")
    case 6:
        print("Stop the program")
import os
print("########################################")
print("#            FILE HANDELING            #")
print("########################################")
def ins():
    print("1. create new file")
    print("2. write text in file")
    print("3. list the files")
    print("4. Delet the file")
    print("5. Rename the file")
    print("6. Stop the program")
c=int(input('Enter ur choice: '))
ins()
def create_file():
    name=input('Enter the file name: ')
    with open(name+".txt","w")as file:
        file.write("Welcome")
    print(name,"created sucessfully..")
def write_file():
    name=input('Enter the file name to Write: ')
    text=input('Type the Content: ')
    with open(name+".txt","a")as file:
        file.write(text)
    print(name,"created sucessfully..")
    while(True):
    ins()
    match c:
        case 1:
            print("creating File")
            create_file()
        case 2:
            print("Edit")
            write_file()
        case 3:
            print("List file")
            files_list=os.listdir(".")
            print(files_list)        
        case 4:
            print("Delet file")
        case 5:
            print("Rename")
        case 6:
            print("Stop the program")
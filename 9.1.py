import os

def main():
  filePath = input("What is the name of the directory you would like to save the file in? : ")
  File_name = input("What is the file name? : ")
  First_name = input("What is your first name? : ")
  Last_name = input("What is your last name? : ")
  Address = input("What is your address? : ")
  Phone_number = input("What is your phone number? : ")
  if os.path.isdir(filePath):
    writeFile = open(os.path.join(filePath,File_name),'w')
    writeFile.close()
    print("")
    print("File contents:")
    print("---------------")
    print("")
    readFile = open(os.path.join(filePath,File_name),'r')
    for line in readFile:
        print(line)
    readFile.close()

  else:
    print("")
    print("===============================================")
    print("")
    print("Sorry that directory doesn't appear to exist...")

main()

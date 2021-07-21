#!/usr/bin/env python3
'''loop through data example to write out to a file'''

#standard library import
import csv

which = input("Do you want manually create a file (1) or read from csv_users.txt (2)? ") 
ans = which

def auto():
    #open csv file data
    with open("csv_users.txt", "r") as csvfile:
        #counter to create unique file
        i = 0
        #loop across open file
        for row in csv.reader(csvfile):
            #increase i by 1 to create a unique file
            i = i + 1
            #this f string says to fill value with i
            filename = f"admin.rc{i}" 

            #open a file via with the file will auto close when no longer indinted
            with open(filename, "w") as rcfile:
                #use the standard library print function to print the data
                #out to the open file open rcfile (open in write mode)
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                print("export OS_USERNAME=" + row[3], file=rcfile)
                print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                print("export OS_PASSWORD=" + row[5], file=rcfile)

    #close all open files

def manual():
    #!/usr/bin/env python3
    outFile = open("admin.rc", "a")
    osAUTH = input("What is the OS_AUTH_URL?")
    print("export OS_AUTH_URL=" + osAUTH, file=outFile)

    print("export OS_IDENTITY_API_VERSION=3", file=outFile)

    osPROJ = input("What is the OS_PROJECT_NAME?")
    print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

    osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME?")
    print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

    osUSER = input("What is the OS_USERNAME?")
    print("export OS_USERNAME=" + osUSER, file=outFile)

    osUSERDOM = input("What is the OS_USER_DOMAIN_NAME?")
    print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

    osPASS = input("What is the OS_PASSWORD?")
    print("export OS_PASSWORD=" + osPASS, file=outFile)
    outFile.close()

def main():

    if ans == "1":
       print(auto())
            
    elif ans == "2":
        print(manual())
    else:
        print("Please type in either 1 or 2")


#print out that all files have been created when the loop is compelted
print("admin.rc files created!")

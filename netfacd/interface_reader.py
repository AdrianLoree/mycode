#!/usr/bin/env python3

import netifaces

def ip():
    ans2 = input("What adaptor are you looking for? ")
    if ans2 == "lo":
#        print('\n********Details of Interface - ' + lo + ' ************')
#        try:
         print('IP: ', end='')  # This print statement will always print IP without an end of line
         print((netifaces.ifaddresses(i)[netifaces.AF_INET])[1]['addr']) # Prints the IP address
#        except:          # This is a new line
#            print('Could not collect adapter information') # Print an error message
    elif ans2 == 'ens3':
        print('\n********Details of Interface - ' + ens3 + ' ************')
        try:
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[1]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    elif ans2 == 'docker0':
        print('\n********Details of Interface - ' + docker + ' ************')            
        try:
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[2]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    else:
        print('Please select lo, ens3, or docker')

def mac():
    ans3 = input("What adaptor are you looking for? ")
    if ans3 == "lo":
        print('\n********Details of Interface - ' + lo + ' ************')
        try:
            print('MAC: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    elif ans3 == 'ens3':
        print('\n********Details of Interface - ' + ens3 + ' ************')
        try:
            print('MAC: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[1]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    elif ans3 == 'docker0':
        print('\n********Details of Interface - ' + docker + ' ************')
        try:    
            print('MAC: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[2]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    else:
        print('Please select lo, ens3, or docker')
def main():
    print(netifaces.interfaces())
    ans = input("Are you looking for MAC or IP? ")
    if ans.lower() == "mac":
        mac()
    elif ans.lower() == "ip":
        ip()
    else:
        print("Please type MAC or IP")

if __name__ == "__main__":
    main()

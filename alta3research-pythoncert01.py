#!/usr/bin/python3
'''Script to print out Magic the Gathering cards
    from a user inputed type'''

#import standard libaries
import datetime
import requests
import pandas

#API variable for url
API = "https://api.magicthegathering.io/v1/"

#date va
date= datetime.datetime.now().strftime("%Y-%m-%d")

# file creation function
def makefile(types, card):
    '''pandas used to print out user input to excel file'''

    #use panada to read the file into dataframe
    cardoutput = pandas.DataFrame.from_dict(card.get("card"))

    #using the setcode inputted it names excel file setcodecards.xlsx
    cardoutput.to_excel(f'{types}-cardlist-{date}.xlsx')
    print("file created!")


#main function of script that will run when the script is run
def main():
    '''loads at runtime'''
    while True:

        #print purpse of script to user
        print('Select a card type from the below:')

        #api request
        resp = requests.get(f"{API}types")

        #api response to display options to user
        ctypes = resp.json()

        #display options
        print(ctypes)

        # take user input
        types = input("What type of cards do you wish to see?\
(example Land, Artifact, etc. type quit to stop): ").capitalize()

        # if user types in value that matches return response to output to file
        if types == ctypes.values:

            #send url request to API
            resptypes = requests.get(f"{API}cards?type={types}")

            #used to show resonse was working
            card = resptypes.json()

            #send data to makefile function
            makefile(types, card)

        # quit the script if user types in quit
        elif types == 'Quit':
            break

        # if input is not in the type of cards warn the user to try again.
        else:
            print('That is not in the list of types! Try again!')

    # test code to make sure
    #   print(card)

if __name__ == "__main__":
    main()

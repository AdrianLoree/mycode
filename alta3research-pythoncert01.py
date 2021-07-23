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
        print(ctypes.get('types'))

        # take user input
        types = input('\n' + "What type of cards do you wish to see?\
(example Land, Artifact, etc. type quit to stop): ").capitalize()

        # if user types in value that matches return response to output to file
        if types in ctypes.get('types'):

            #api request
            resp = requests.get(f"{API}types")
            
            #send url request to API
            resptypes = requests.get(f"{API}cards?type={types}")

            #used to show resonse was working
            card = resptypes.json()

            #use panada to read the file into dataframe
            cardoutput = pandas.DataFrame.from_dict(card.get("card"))

            #using the setcode inputted it names excel file setcodecards.xlsx
            cardoutput.to_excel(f'{types}-cardlist-{date}.xlsx')

            #tell user file is made
            print("file created!" + '\n')

        # quit the script if user types in quit
        elif types == 'Quit':
            break

        # if value is not in types tell the user
        else:
            print('That is not a type please try again!' + '\n')

    # test code to make sure
    #   print(card)

if __name__ == "__main__":
    main()

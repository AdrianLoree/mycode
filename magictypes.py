#!/usr/bin/python3
'''Script to print out Magic the Gathering cards
    from a user inputed type'''
#import standard libaries
import requests
import pandas
import crayons

#API variable for url
API = "https://api.magicthegathering.io/v1/"

#main function of script that will run when the script is run
def main():
    '''loads at runtime'''

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
(example Land, Artifact, etc.) ").capitalize()

    #send url request to API
    resptypes = requests.get(f"{API}cards?type={types}")

    #used to show resonse was working
    card = resptypes.json()

    # test output
#   print(card)

    #use panada to read the file into dataframe

    cardoutput = pandas.DataFrame.from_dict(get.json("card"))

    #using the setcode inputted it names excel file setcodecards.xlsx
    cardoutput.to_excel(f'{types}-cardlist.xlsx')

    print(crayons.green("file created!"))

if __name__ == "__main__":
    main()

#!/usr/bin/python3

import requests
import pandas
import json

API = "https://api.magicthegathering.io/v1/"

def main():
    #print purpse of script to user
    print('Select a card type from the below:')
    #api request
    resp = requests.get(f"{API}types")
    #api response to display options to user
    ctypes = resp.json()
    #display options
    print(ctypes)
    # take user input
    types = input("What type of cards do you wish to see? (example Land, Artifact, etc.) ").capitalize()
    #send url request to API
    resptypes = requests.get(f"{API}cards?type={types}")

    #used to show resonse was working
    #    card = resptypes.json()

    #    print(card)

    #change json response to text file?
    cards = resptypes.text
    
    #load the json file
    
    json_dict= json.loads(cards)
    
    #use panada to read the file into dataframe
    
    cardoutput = pandas.DataFrame.from_dict(json_dict["cards"])
    
    #using the setcode inputted it names excel file setcodecards.xlsx
    cardoutput.to_excel(f'{types}-cardlist.xlsx')

    print("file created!")

if __name__ == "__main__":
    main()

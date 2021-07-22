#!/usr/bin/python3

import requests
import pandas
import json

API = "https://api.magicthegathering.io/v1/"

def main():
    
    print('Select a card type from the below:')

    resp = requests.get(f"{API}types")

    ctypes = resp.json()

    print(ctypes)

    types = input("What type of cards do you wish to see? ").lower()
   
    resptypes = requests.get(f"{API}cards?{type}")

    cards = resptypes.text
    #load the json file
    json_dict= json.loads(cards)
    #use panada to read the file into dataframe
    cardoutput = pandas.DataFrame.from_dict(json_dict["cards"])
    #using the setcode inputted it names excel file setcodecards.xlsx
    cardoutput.to_excel(f'{types}-cards.xlsx')

    

if __name__ == "__main__":
    main()

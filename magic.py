#!/usr/bin/env python3
'''output cards from MTG set to a excel file'''

#import standard libraries
import requests
import pandas
import json

#api url to make the request
API = "https://api.magicthegathering.io/v1/"

def main():
    '''loads at runtime'''
    #asks the user for the card set code of the MTG they wish to see
    setcode = input("Which is the code of the set you want to see? ").lower()
    
    #make the API request with the inputted setcode
    resp= requests.get(f"{API}cards?set={setcode}")
    
    #take json response and turn it into a text file?
    cards = resp.text
    #load the json file
    json_dict= json.loads(cards)
    #use panada to read the file into dataframe
    cardoutput = pandas.DataFrame.from_dict(json_dict["cards"])
    #using the setcode inputted it names excel file setcodecards.xlsx
    cardoutput.to_excel(f'{setcode}cards.xlsx')
     
#best practices for ending main function
if __name__ == "__main__":
    main()

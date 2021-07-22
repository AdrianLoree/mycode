#!/usr/bin/env python3

import requests
import pandas
import json

API = "https://api.magicthegathering.io/v1/"

def main():

    setcode = input("Which is the code of the set you want to see? ").lower()

    resp= requests.get(f"{API}cards?set={setcode}")

    cards = resp.text
    json_dict= json.loads(cards)
    cardoutput = pandas.DataFrame.from_dict(json_dict["cards"])

    cardoutput.to_excel("cards.xlsx")
     

if __name__ == "__main__":
    main()

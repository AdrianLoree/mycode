#!/usr/bin/env python3
import requests
import re

def main():
    counter= 0
    while True:
        print("Where should we search? type quit to stop searching")
        url = input()   
        if url != "quit":
            print("Where should we search? type quit to stop searching")
#            url = input()
#           print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
            searchFor = input()
            resp = requests.get(f'{url}')
            searchMe = resp.text
            if re.findall(searchFor, searchMe):
                counter = counter + 1
                print("Found a match!")
                print("Found this many matches:", counter)
            else:
                print("No match!")

        elif url == 'quit':
            break
           
if __name__ == "__main__":
    main()

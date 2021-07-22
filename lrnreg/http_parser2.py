#!/usr/bin/env python3
import requests
import re

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
searchFor = input()
resp = requests.get(f'{url}')
searchMe = resp.text
if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")
                                               

#!/usr/bin/env python3
'''json challenge 2 july 21'''
#import standard library
import requests
import json
#API call to make
ASTROS = "http://api.open-notify.org/astros.json"

#request to get api call
resp = requests.get(ASTROS)

#print out json response
json_from_astro = resp.json()
print(json_from_astro)
print(json_from_astro.get("people")[0].get("name") + " is the astronaut who currently has been in space the longest and they are on the " + json_from_astro.get("people")[0].get("craft"))


#!/usr/bin/env python

import json
import requests


def main():
    jsondata = requests.get("http://api.open-notify.org/astros.json")
    astros = jsondata.json()
    print("here is the data for astronauts in space: \n")
    print(astros['people'])
    print("current status in readable format:")
    for naut in astros['people']:
        print(naut['name'] + " is onboard the " + naut['craft'])
    print("app complete")

main()

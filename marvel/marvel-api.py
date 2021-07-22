#!/usr/bin/env python3

import requests

MARVEL = "http://developer.marvel.com/v1/public/characters?name=Captain"

def main():

    with open("../../marvelpub.cred", 'r') as marvelkfile:
        marvelkey = marvelkfile.read().strip('\n')

    with open("../../marvel.cred", 'r') as marvelhfile:
        marvelhash = marvelhfile.read().strip('\n')
        
    resp = requests.get(f"{MARVEL}&apikey={marvelkey}&hash={marvelhash}")
    if resp.status_code !=200:
        print("Uhoh!")
    else:
        print(resp.json())
main()

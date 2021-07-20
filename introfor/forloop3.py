#!/usr/bin/env python3
import json

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for item in farms:
    for key,value in item.items():
        print(value)
        #for x in farms:
#    print(x.get("name")

#for x in farms:
#    print(x)
#print("\nOur loop has ended")

    

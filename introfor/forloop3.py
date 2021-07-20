#!/usr/bin/env python3
'''for loop displaying custom code 01 of lab 24'''
#import standard library
import json

#data set to disaply
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#display name of farm and what they produce
#for item in farms:
#    for key,value in item.items():
#        print(value)
for x in farms:
    print(x.get("name") "-" x.get("agriculture"))

for x in farms:
    print(x.get("agriculture"))

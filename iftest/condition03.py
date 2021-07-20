#!/usr/bin/env python3
'''check hostname against expected value'''

#collect the input from teh user
hostname = input("What value should we set for hostname?")

# use the lower method to test if input value matches expected value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

#Always print out to the user
print("exiting the script")

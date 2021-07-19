#!/usr/bin/env python3

#open file
filelist = open("challenege.txt", "r")

#print list from file
print(filelist.read().splitlines())

print(type(filelist.read().splitlines()))

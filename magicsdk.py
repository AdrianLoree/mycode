#!/usr/bin/python3

from mtgsdk import Card
from mtgsdk import Set
cardfind = input("What set do you wish to see ? ie 4ed ")

sets = Set.find(f'{cardfind}')
print(sets.name, sets.code)
cards = Card.where(set_name=f'{sets.name}')

#print(cards.text)

print(cards)

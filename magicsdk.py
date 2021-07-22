#!/usr/bin/python3

from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

#setcode = input("What set do you want to see cards from ? (4ed?) ")

#sets = Set.where(f'code={setcode}').all()
#sets = Set.find('ktk')
card = Card.find(386616)

print(card)

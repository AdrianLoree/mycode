#!/usr/bin/python3

from mtgsdk import Card

card = Card.find(386616)
cards = Card.where(set='ktk').where(subtypes='warrior,human').all()

print(card)
print(cards)


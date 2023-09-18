#!python3
import random

ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['C','D','H','S']

clubs = [(i + "C") for i in ranks]
diamonds = [(i + "D")for i in ranks]
hearts = [(i + "H")for i in ranks]
spades = [(i + "S")for i in ranks]

cards = [clubs,diamonds,hearts,spades]


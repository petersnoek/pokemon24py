#!/usr/bin/env python3

from charmander import Charmander


# Game
print("*** PokeBattle ***")

# Game loop
isGameRunning = True
while isGameRunning:
    answer = input("Voer een naam in (of type 'quit' om te stoppen): ")
    if answer == 'quit':
        quit()

    c = Charmander(answer)
    c.battlecry()


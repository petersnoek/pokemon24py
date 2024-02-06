#!/usr/bin/env python3

from charmander import Charmander


# 1. The player start the game.
# 2. The player gives a name to a charmander.
# 3. The charmander does its battle cry for ten times.
# 4. The player can give a new name to the same charmander.
# 5. The charmander does its battle cry for ten times.
# 6. Repeat 4 and 5 until the player quits the game.

# Game
print("*** PokeBattle ***")

answer = input("Type 'start' om te beginnen (of type 'quit' om te stoppen): ")
if answer == 'quit':
    quit()

# Game loop
isGameRunning = True
while isGameRunning:
    answer = input("Voer een naam in (of type 'quit' om te stoppen): ")
    if answer == 'quit':
        quit()

    c = Charmander(answer)
    for x in range(10):
        c.battlecry()


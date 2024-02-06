class Charmander:
    nickname = ""
    strength = ""
    weakness = ""

    def __init__(self, new_nickname):
        self.nickname = new_nickname
        self.strength = "fire"
        self.weakness = "water"

    def battlecry(self):
        for x in range(10):
            print(self.nickname.upper() + "!!!")

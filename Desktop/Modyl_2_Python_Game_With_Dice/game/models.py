import random
from game.settings import DICE_MIN, DICE_MAX

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        return random.randint(DICE_MIN, DICE_MAX)

    def update_score(self, points):
        self.score += points



class Computer:
    def __init__(self):
        self.name = "Computer"
        self.score = 0

    def roll_dice(self):
        return random.randint(DICE_MIN, DICE_MAX)

    def update_score(self, points):
        self.score += points
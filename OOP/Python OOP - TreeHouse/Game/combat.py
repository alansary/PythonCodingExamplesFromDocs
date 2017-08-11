#!/usr/bin/env pythonn3
import random

#Reusing Code
    # Don't Repeat Yourself (DRY)
    # Write Everything Twice (WET) (We Enjoy Typing)

# Keep your code DRY (Don't Repeat Yourself)
    # Group common  operations into functions
    # Group common functionality into classes

class Combat:
    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4

#!/usr/bin/env python3
import random
from combat import Combat


# If we want to override inherited method completely, we just redefine in our class


class Character(Combat):
    attack_limit = 10 # Overriding inheritance (Making user attacks succeed more often)
    experience = 0
    base_hit_points = 10

    # since some weapons are more strong than others we will give special weapons more chance to attack (Bonus)
    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    def set_weapon(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's': return 'sword'
            elif weapon_choice == 'a': return 'axe'
            else: return 'bow'
        else:
            return self.set_weapon()

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.set_weapon()
        self.hit_points = self.base_hit_points
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def leveled_up(self):
        return self.experience >= 5
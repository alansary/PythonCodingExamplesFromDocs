#!/usr/bin/env python3
import random
from combat import Combat


COLORS = ['yellow', 'red', 'green', 'blue']

class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    sound = 'roar'
    weapon = 'sword'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_hit_points, self.max_hit_points)
        self.color = random.choice(COLORS)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} <Hit Points: {}\tExperience: {}\tColor: {}\tWeapon: {}\tSound: {}>'.format(self.__class__.__name__,
                                                                                                      self.hit_points,
                                                                                                      self.experience,
                                                                                                      self.color,
                                                                                                      self.weapon,
                                                                                                      self.sound)

    def battlecry(self):
        return self.sound.upper()


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = "raaaaaaaaar"


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = "growl"


class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = "squeak"


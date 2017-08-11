#!/usr/bin/env python3
import random

def main():
    jubjub = Monster(color = "red", sound = "tweet", adjective = "manxsome")
    print(jubjub)
    print(jubjub.hit_points, jubjub.weapon, jubjub.color, jubjub.sound, jubjub.battlecry(), jubjub.adjective)
    jabberwock = Monster()
    print(jabberwock)
    print(jabberwock.hit_points, jabberwock.weapon, jabberwock.color, jabberwock.sound, jabberwock.battlecry())
    azog = Goblin()
    print(azog)
    print(azog.hit_points, azog.color, azog.weapon, azog.sound, azog.experience, azog.battlecry())
    snaga = Troll()
    print(snaga)
    print(snaga.hit_points, snaga.color, snaga.weapon, snaga.experience, snaga.battlecry())
    pete = Dragon()
    print(pete)
    print(pete.hit_points, pete.color, pete.weapon, pete.experience, pete.battlecry())

COLORS = ['yellow', 'red', 'blue', 'green']


# Monster is the parent of Goblin; however, it has a parent class too (it is a class after all)
# This argument object tells us that some other class inherits the attributes and the methods of this class
class Monster(object):
    # Initializing the attributes
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = "sword"    # This attribute is shared along all instances of this class
    sound = "roar"

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)
            # setattr(object to set the attribute on (instance)(self), the attribute we want to set, the value to give that attribute)

    def battlecry(self):
        return self.sound.upper()


    # is much like __init__ but controls how our instances print themselves (gets called whenever something is converted to a string)
    # __class__ The class the object is an instance of
    # __name__ The string version of the class name
    # The following format will be returned if we wanted to print any object of this class of a class that is inherited from this class
    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)


# Goblin is a subclass of the class Monster
# Goblin has all of the attributes of Monster and all the methods of Monster too unless we changed them
class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = "squeak"


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = "growl"


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = "raaaaaaaaar"


if __name__ == "__main__": main()
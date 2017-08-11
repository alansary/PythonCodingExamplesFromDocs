#!/usr/bin/env python3
# Method: A function within a class (Action).
# Attribute: A behaviour of an object within a class.
# Class: Is the blueprint that contains the object attributes and methods.
# Object: Is an instance of the class (copy of the class, but we can change each instance independently)
def main():
    jubjub = Monster(color = 'red', sound = 'tweet')
    print(jubjub.battlecry(), jubjub.sound, jubjub.color, jubjub.weapon, jubjub.hit_points)
class Monster():
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get('hit_points', 1)
        self.weapon = kwargs.get('weapon', 'sword')
        self.color = kwargs.get('color', 'yellow')
        self.sound = kwargs.get('sound', 'roar')
    def battlecry(self):
        return self.sound.upper()
'''
    # print(Monster.hit_points, Monster.color, Monster.weapon)
        # This will work if we defined these attributes in the class itself not within __init__ or any other method
    jubjub = Monster()
    print(jubjub.hit_points, jubjub.color, jubjub.weapon)
    jubjub.hit_points = 2
    jubjub.color = "red"
    jubjub.weapon = "gun"
    print(jubjub.hit_points, jubjub.color, jubjub.weapon)
    jabberwock = Monster()
    print(jabberwock.hit_points, jabberwock.color, jabberwock.weapon)
    jubjub.color = "yellow"
    jubjub.weapon = "sword"
    print(jubjub.color, jubjub.weapon)
    print(jubjub.battlecry(), jabberwock.battlecry())
    jubjub.sound = "tweet"
    print(jubjub.battlecry())
    print(jubjub.hit_points, jubjub.color, jubjub.sound, jubjub.weapon, jubjub.battlecry())
    print(jabberwock.hit_points, jabberwock.color, jabberwock.sound, jabberwock.weapon, jabberwock.battlecry())
    slimey = Monster(5, "blue", "sword", "glug")
    print(slimey.hit_points, slimey.weapon, slimey.color, slimey.sound, slimey.battlecry())
    oger = Monster(10)
    print(oger.hit_points, oger.weapon, oger.color, oger.sound, oger.battlecry())
# Monsterr class
# The Capital M is a Case Convention
class Monster:
    # __init__ is called automatically whenever we create a new object of our class (initializing the object's attributes)
    # dander init (dander is the double underscore)
    # self is a reference to the instantiated object (each reference has its own attribute values)
    def __init__(self, hit_points = 5, color = "yellow", weapon = "sword", sound = "roar"):
        # Attributes of each object of the Monster class
        self.hit_points = hit_points
        self.color = color
        self.weapon = weapon
        self.sound = sound
    # Methods (Actions) of each object of the class
    def battlecry(self):
        return self.sound.upper()
'''
if __name__ == "__main__": main()
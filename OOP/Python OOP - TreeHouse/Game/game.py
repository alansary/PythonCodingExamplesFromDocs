#!/usr/bin/env python3
import sys
from character import Character
from monster import Dragon
from monster import Troll
from monster import Goblin


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def set_dodge_ans(self):
        ans = input("Do you want to dodge (Y/N)? ").lower()
        if ans in 'yn':
            return ans
        else:
            return self.set_dodge_ans()

    def sub_hit_points(self):
        self.player.hit_points -= 1

    def monster_turn(self):
        # Check to see if the monster attacks
        # If so, tell the player
            # Check if the player wants to dodge
            # If so, see if the dodge is successful
            # If it is, move on
            # If it's not, remove one player hit point
        # If the monster isn't attacking, tell that to the player too.
        if self.monster.attack():
            print(self.monster, "is attacking")
            ans = self.set_dodge_ans()
            if ans == 'y':
                if self.player.dodge():
                    print("You dodged the attack")
                else:
                    print("You got hit anyway!")
                    self.sub_hit_points()
            elif ans == 'n':
                print("{} hit you for one point!".format(self.monster))
                self.sub_hit_points()
        else:
            print(self.monster, "is not attacking this turn.")

    def set_ans(self):
        ans = input("You're the boss ([A]ttack, [R]est, [Q]uit)? ").lower()
        if ans in 'arq':
            return ans
        else:
            return self.set_ans()

    def player_turn(self):
        # Let the player attack, rest, or quit
        # If they attack:
            # see if the attack is successful
                # If so, see if the monster godges
                    # If dodged, print that
                    # If not dodged, subtract the right num of hit points from the monster
            # If not a good attack, tell the player
        # If they rest:
            # Call the player.rest() method
        # If they quit, exit the game
        # If they pick anything else, re-run this method
        ans = self.set_ans()
        if ans == 'a':
            print("You are attacking {}!".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print(self.monster, "dodged your attack")
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You hit {} with your {}!".format(
                        self.monster, self.player.weapon
                    ))
            else:
                print("You missed!")
        elif ans == 'r':
            self.player.rest()
        else:
            sys.exit()

    def cleanup(self):
        # If the monster has no more hit points:
            # Up the player's experience
            # Print a message
            # Get a new monster
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("Congratulations, you killed {}".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print("\n"+'='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20) # - is called hyphen
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()


# Running the game:
Game()
#!/usr/bin/python3
# switch.py by Mohamed Alansary
# This is an exercise file from Python 3 Training
# Copyright 2016 Alansary Group

def main():
    choices = dict(
        one = "one",
        two = "two",
        three = "three",
        four = "four",
        five = "five"
    )
    v = "one"
    print(choices.get(v, "other"))
    v = "seven"
    print(choices.get(v, "other"))

if __name__ == "__main__": main()

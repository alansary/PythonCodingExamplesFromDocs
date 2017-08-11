#!/usr/bin/env python3

# Often used in conditional statements, all and any take a list as an argument, and return True if all or any
# (respectively) of their arguments evaluates to True (and False otherwise).
# The function enumerate can be used to iterate through the values and indices of a list simultaneously.


def main():
    nums = [55, 44, 33, 22, 11]
    print([i > 5 for i in nums]) # This is a list of boolean values
    if all([i > 5 for i in nums]):
        print("All larger than 5")
    print([i % 2 == 0 for i in nums]) # This is a list of boolean values
    if any([i % 2 == 0 for i in nums]):
        print("At least one is even")
    for v in enumerate(nums):
        print(v)
if __name__ == "__main__": main()

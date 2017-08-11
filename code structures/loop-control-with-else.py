#!/usr/bin/env python3
def main():
    test_string = "This is a string"
    for c in test_string:
        print(c, end = '')
    else: # The sweet of else gets run whenever the condition of the for loop becomes completely false
    # (the iterator out of stuff to iterate)
        print("\nelse")
    print()
    i = 0
    while i < len(test_string):
        print(test_string[i], end = '')
        i += 1
    else: # When the condition of the while loop becomes false, the block of else is executed
        print("\nelse")
    print('')
    # Also else block is executed if the condition is false in the first place
    while False:
        print("This is false")
    else:
        print("The else block is executed")
if __name__ == "__main__": main()

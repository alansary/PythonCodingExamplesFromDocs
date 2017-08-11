#!/usr/bin/env python3
def main():
    test_list = [x for x in range(1, 100, 2)]
    # enumerate returns two values, the first value is an index and the second value is the value from the iterator
    for index, value in enumerate(test_list):
        print("The value {1} is at the index {0}".format(index, value))
    test_string = "This is a string"
    for i, v in enumerate(test_string):
        if v == 's':
            print(i, v)
if __name__=="__main__": main()
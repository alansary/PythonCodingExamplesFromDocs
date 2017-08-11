#!/usr/bin/env python3

# Trying to create a list in a very extensive range will result in a MemoryError.


def main():
    try:
        my_list = [2*i for i in range(10 ** 100)]
    except MemoryError as e:
        print(e)
if __name__ == "__main__": main()

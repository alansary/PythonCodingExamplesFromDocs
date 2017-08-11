#!/usr/bin/env python3

# Using with statement will create a temporary variable (often called f), which is only accessible in the indented block
# of the with statement.


def main():
    with open('with_clause.txt', 'r') as f:
        print(f.readline())
    try:
        print(f.readline()) # raises ValueError: I/O operation on closed file.
    except ValueError as e:
        print(e)
    print(f)

if __name__ == "__main__": main()

#!/usr/bin/env python3
def main():
    a, b = 0, 1
    print("This is true" if a < b else "This is false")
    a, b = 1, 0
    v = "This is true" if a < b else "This is false"
    print(v)
if __name__ == "__main__": main()
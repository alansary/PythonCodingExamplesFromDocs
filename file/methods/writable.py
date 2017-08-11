#!/usr/bin/env python3

'''
 |  writable(self, /)
 |      Return whether object was opened for writing.
 |      
 |      If False, write() will raise OSError.
'''

def main():
    fileHandle = open("writable1.txt", 'r')
    print(fileHandle.writable()) # False
    fileHandle = open("writable2.txt", 'w')
    print(fileHandle.writable()) # True
    fileHandle = open("writable3.txt", 'a')
    print(fileHandle.writable()) # True
    fileHandle = open("writable4.txt", 'x')
    print(fileHandle.writable()) # True
    fileHandle = open("writable5.txt", 'r+')
    print(fileHandle.writable()) # True
    fileHandle = open("writable6.txt", 'w+')
    print(fileHandle.writable()) # True
    fileHandle = open("writable7.txt", 'a+')
    print(fileHandle.writable()) # True
    fileHandle = open("writable8.txt", 'x+')
    print(fileHandle.writable()) # True

if __name__ == "__main__": main()

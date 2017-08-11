#!/usr/bin/env python3

'''
 |  readable(self, /)
 |      Return whether object was opened for reading.
 |      
 |      If False, read() will raise OSError.
'''

def main():
    fileHandle = open("readable1.txt", 'r')
    print(fileHandle.readable()) # True
    fileHandle = open("readable2.txt", 'w')
    print(fileHandle.readable()) # False
    fileHandle = open("readable3.txt", 'a')
    print(fileHandle.readable()) # False
    fileHandle = open("readable4.txt", 'x')
    print(fileHandle.readable()) # False
    fileHandle = open("readable5.txt", 'r+')
    print(fileHandle.readable()) # True
    fileHandle = open("readable6.txt", 'w+')
    print(fileHandle.readable()) # True
    fileHandle = open("readable7.txt", 'a+')
    print(fileHandle.readable()) # True
    fileHandle = open("readable8.txt", 'x+')
    print(fileHandle.readable()) # True

if __name__ == "__main__": main()

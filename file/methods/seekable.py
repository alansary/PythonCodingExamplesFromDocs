#!/usr/bin/env python3

'''
     |  seekable(...)
     |      Return whether object supports random access.
     |      If False, seek(), tell() and truncate() will raise UnsupportedOperation.
     |      This method may need to do a test seek().
'''

def main():
    fileHandle = open("seekable1.txt", 'r')
    print(fileHandle.seekable()) # True
    fileHandle = open("seekable2.txt", 'w')
    print(fileHandle.seekable()) # True
    fileHandle = open("seekable3.txt", 'a')
    print(fileHandle.seekable()) # True
    fileHandle = open("seekable4.txt", 'x')
    print(fileHandle.seekable()) # True
    fileHandle = open("seekable5.txt", 'r+')
    print(fileHandle.seekable()) # True
    fileHandle = open("seekable6.txt", 'w+')
    print(fileHandle.seekable()) # True
    fileHandle = open("seekable7.txt", 'a+')
    print(fileHandle.seekable()) # True
    fileHandle = open("seekable8.txt", 'x+')
    print(fileHandle.seekable()) # True

if __name__ == "__main__": main()

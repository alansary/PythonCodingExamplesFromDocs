#!/usr/bin/env python3

'''
'r' mode raises IOError if the file does not exist.
'''

def main():
    try:
        fileHandle = open("readMode0.txt")
        for line in fileHandle:
            print(line, end = '')
    except IOError as e:
        print(e)

    fileHandle = open("readMode1.txt")
    for line in fileHandle:
        print(line, end = '')
    print("-" * 80)

    fileHandle = open("readMode2.txt", 'r')
    for line in fileHandle:
        print(line, end = '')
    print("-" * 80)

    fileHandle = open("readMode3.txt", 'r+')
    fileHandle.seek(0, 2)
    fileHandle.write("Hi, there!\n");
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')
    print("-" * 80)

    fileHandle = open("readMode4.txt", 'rt')
    for line in fileHandle:
        print(line, end = '')
    print("-" * 80)

    fileHandle = open("readMode5.txt", 'rb')
    for line in fileHandle:
        print(line, end = '')
    print("-" * 80)

    fileHandle = open("readMode6.txt", 'rt+')
    fileHandle.seek(0, 2)
    fileHandle.write('Hello, its me!\n')
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')
    print('-' * 80)

    fileHandle = open("readMode7.txt", 'rb+')
    fileHandle.seek(0, 2)
    fileHandle.write(b'Hello, its me!\n')
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')
    print('-' * 80)

if __name__ == "__main__": main()

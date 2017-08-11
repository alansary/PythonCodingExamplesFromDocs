#!/usr/bin/env python3

'''
'w' mode truncates the file if the file does exist and creates the file if the file does not exist.
'''

def main():
    fileHandle = open("writeMode1.txt", 'w')
    fileHandle.write("This is the fourth line\n")
    
    fileHandle = open("writeMode2.txt", 'w')
    fileHandle.write("This is the first line\n")
    fileHandle.write("This is the second line\n")
    fileHandle.write("This is the third line\n")

    fileHandle = open("writeMode3.txt", 'wt')
    fileHandle.write("This is the first line\n")

    fileHandle = open("writeMode4.txt", 'wb')
    fileHandle.write(b'This is the first line\n')

    fileHandle = open("writeMode5.txt", 'w+')
    fileHandle.write("This is the first line\n")
    fileHandle.write("This is the second line\n")
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

    fileHandle = open("writeMode6.txt", 'wt+')
    fileHandle.write("This is the first line\n")
    fileHandle.write("This is the second line\n")
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

    fileHandle = open("writeMode7.txt", 'wb+')
    fileHandle.write(b'This is the first line\n')
    fileHandle.write(b'This is the second line\n')
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

if __name__ == "__main__": main()

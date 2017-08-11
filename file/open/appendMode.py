#!/usr/bin/env python3

'''
'a' mode, if the file does not exist it will be created and if it does exist it will append to it. In append mode the file is opened for writing, to open it for reading, we must add '+'.
'''

def main():
    fileHandle = open("appendMode1.txt", 'a')
    fileHandle.write("This is the fourth line\n")
    fileHandle.write("This is the sixth line\n")

    fileHandle = open("appendMode2.txt", 'at')
    fileHandle.write("This is the fourth line\n")
    fileHandle.write("This is the sixth line\n")

    fileHandle = open("appendMode3.txt", 'ab')
    fileHandle.write(b"This is the fifth line\n")
    fileHandle.write(b"This is the sixth line\n")

    fileHandle = open("appendMode4.txt", 'a+')
    fileHandle.write("This is the fifth line\n")
    fileHandle.write("This is the sixth line\n")
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

    fileHandle = open("appendMode5.txt", 'at+')
    fileHandle.write("This is the fifth line\n")
    fileHandle.write("This is the sixth line\n")
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

    fileHandle = open("appendMode6.txt", 'ab+')
    fileHandle.write(b'This is the fifth line\n')
    fileHandle.write(b'This is the sixth line\n')
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

if __name__ == "__main__": main()

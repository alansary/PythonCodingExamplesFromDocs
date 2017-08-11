#!/usr/bin/env python3

'''
'x' raises a FileExistsError if the file does exist and creates then opens the file in writing mode if the file does not exist.
'''

def main():
    try:
        fileHandle = open('xMode1.txt', 'x')
    except FileExistsError as e:
        print(e)

    fileHandle = open("xMode2.txt", 'x')
    fileHandle.write("This is the first line\n")
    fileHandle.write("This is the second line\n")

    fileHandle = open("xMode3.txt", 'xt')
    fileHandle.write("This is the first line\n")
    fileHandle.write("This is the second line\n")

    fileHandle = open("xMode4.txt", 'xb')
    fileHandle.write(b'This is the first line\n')
    fileHandle.write(b'This is the second line\n')

    fileHandle = open("xMode5.txt", 'x+')
    fileHandle.write("This is the first line\n")
    fileHandle.write("This is the second line\n")
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

    fileHandle = open("xMode6.txt", 'x+t')
    fileHandle.write("This is the first line\n")
    fileHandle.write("This is the second line\n")
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

    fileHandle = open("xMode7.txt", 'x+b')
    fileHandle.write(b'This is the first line\n')
    fileHandle.write(b'This is the second line\n')
    fileHandle.seek(0, 0)
    for line in fileHandle:
        print(line, end = '')

if __name__ == "__main__": main()

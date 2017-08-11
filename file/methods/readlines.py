'''
     |  readlines(...)
     |      Return a list of lines from the stream.
     |      hint can be specified to control the number of lines read: no more
     |      lines will be read if the total size (in bytes/characters) of all
     |      lines so far exceeds hint.
'''
fileObject = open('readlines.txt', 'r')
print(fileObject, "is a file object")
print("Reading the first two lines in the file:")
for line in fileObject.readlines(23):
    print(line, end = '')
print("Reading the next lines till EOF:")
for line in fileObject.readlines():
    print(line, end = '')


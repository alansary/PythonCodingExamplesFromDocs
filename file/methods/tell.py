'''
 |  tell(self, /)
 |      Return current stream position.
'''
fileObject = open('tell.txt', 'r')
print(fileObject, "is a file object")
print("The current position is %d" % fileObject.tell())
print("The first line is %s" % fileObject.readline())
print("The current position is %d" % fileObject.tell())
print("The second line is %s" % fileObject.readline())
print("The current position is %d" % fileObject.tell())
print("The third line is %s" % fileObject.readline())
print("The current position is %d" % fileObject.tell())


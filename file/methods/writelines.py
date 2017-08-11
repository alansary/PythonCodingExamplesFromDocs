import string
fileObject = open('writelines.txt', 'a+')
print(fileObject, 'is a file object')

test_list = ['test line number one', 'test line number 2']
print("Writing lines from the iterable %r" % test_list)
fileObject.writelines(test_list)
fileObject.write('\n')

test_tuple = ('test line number three', 'test line number four')
print("Writing lines from the iterable %r" % (test_tuple,))
fileObject.writelines(test_tuple)
fileObject.write('\n')

test_dict = {'test line number five':5, 'test line number six':6}
print("Writing lines from the iterable %r" % test_dict)
fileObject.writelines(test_dict)
fileObject.write('\n')

test_set = set(['test line number seven', 'test line number eight'])
print("Writing lines from the iterable %r" % test_set)
fileObject.writelines(test_set)
fileObject.write('\n')

test_string = string.punctuation
print("Writing lines from the iterable %r" % test_string)
fileObject.writelines(test_string)
fileObject.write('\n')

test_zip = zip(range(1, 100), "This is a string")
print("Writing lines from the iterable %r" % test_zip)
fileObject.writelines(str(x) for x in test_zip)
fileObject.write('\n')

test_range = range(1, 11)
print("Writing lines from the iterable %r" % test_range)
fileObject.writelines(str(x) for x in test_range)
fileObject.write('\n')

print("Check the file now...")


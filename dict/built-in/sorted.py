'''
sorted(...)
    sorted(iterable, key=None, reverse=False) --> new sorted list of keys
'''
my_dictionary = {1:"This is one", 2:"This is two", 4:"This is four", 3:"This is three", 0.3:"This is a 0.3", 1.32:"This is a 1.32"}
print("The dictionary is %r" % my_dictionary)
print("The items of the dictionary are:")
for key in my_dictionary:
    print("Key: %r\tValue: %r" % (key, my_dictionary[key]))
print("The items of the dictionary sorted are:")
for key in sorted(my_dictionary):
    print("key: %r\tValue: %r" % (key, my_dictionary[key]))


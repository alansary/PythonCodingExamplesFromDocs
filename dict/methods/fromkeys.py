import string
# fromkeys()
'''
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
'''
	# The items in the iterable must be hashable (immutable) and contain hashable (immutable) items as well
test_string = "This is a string" # Iterate through the characters of the string
# test_list = [range(100, -1, -5)] # It will consider test_list contains only one item range(100, -1, -5)
test_list = ["This", 't', 1, 1.5, (1, 2), False] # Iterate through the items of the list (Integers)
test_tuple = ((1, 2, 3), "This is a string", 'x', 2, 2.5, True)
	# Iterate through the items of the tuple (tuple, str, str, int, float, tuple, bool)
test_rangeObj = range(0, 101, 10) # Iterate through the items of the range object (integers)
test_dict = {"One":1, "Two":2, True:1, False:0, "list":[(1, 2), 2, 3.5]}
test_zip = zip("This is a string", range(1, 100), ['x', 'y', 'z'], ("This", "is", "2", 1)) # Iterate through the items of the zip function (4-tuples)
punc = string.punctuation # Iterate through the punctuations
dictionary = {}
print("Creating a dictionary from the keys of the iterable %s" % test_string)
dictionary = dictionary.fromkeys(test_string)
print("The dictionary is %r" % dictionary)
print("Creating a dictionary from the keys of the iterable %r" % test_list)
dictionary = dictionary.fromkeys(test_list, None)
print("The dictionary is %r" % dictionary)
print("Creating a dictionary from the keys of the iterable %r" % (test_tuple,)) # To print only one tuple, enclose it within () and put ',' at the end
dictionary = dictionary.fromkeys(test_tuple, 'X')
print("The dictionary is %r" % dictionary)
print("Creating a dictionary from the keys of the iterable %r" % test_rangeObj)
dictionary = dictionary.fromkeys(test_rangeObj, 0)
print("The dictionary is %r" % dictionary)
print("Creating a dictionary from the keys of the iterable %r" % test_dict)
dictionary = dictionary.fromkeys(test_dict, False)
print("The dictionary is %r" % dictionary)
print("Creating a dictionary from the keys of the iterable %r" % test_zip)
dictionary = dictionary.fromkeys(test_zip, ['x', 1, True])
print("The dictionary is %r" % dictionary)
print("Creating a dictionary from the keys of %s" % punc)
dictionary = dictionary.fromkeys(punc)
print("The dictionary is %r" % dictionary)


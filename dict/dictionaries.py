# dict()
'''
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
'''
'''
    - Dictionaries are mappings, it contains a set of keys and values, the association of a key and a valure is called a key-value pair(item).
    - dict is a mapping from keys to values where each key maps to a value.
    - Dictionaries are mutable, you can access the values of the keys and reassign them. The order of items in a dictionary is unpredictable.
Notice: Assigning more than one value to a specific key "repeating a specific key" is not a syntax error, but it is better not to do so because the one that will appear will be unpredictable, also it is better not to use the value of a key as another key because the behavior will be unpredictable.However you can assign the same value to more than one key "repeating a specific value".
    - A function (mapping) f from A to B is a relation that assigns for each element of A a unique element of B.
    - The key-value pair can be of any data type, we can mix different types in a dictionary for both the keys and values.
    - We cannot make any unhashable type as a key in our dictionary, dictionary is implemented using a hashtable and that means that the keys have   to be hashable (immutable).
    - hashable type:
A type that has a hash function. Immutable types like integers, floats and strings are hashable; mutable types like lists and dictionaries are not.
'''
	# Dictionaries are iterables of key-value pairs.
	# Dictionaries are mutable, and the order of the key-value pairs is unpredictable.
	# Note that: The keys of the dict must be hashable (immutable) and contain hashable (immutable) items as well.
    # You can initialize a dictionary from a list of 2-tuples or even the zip object over two iterables which results in a list of 2-tuples
#Note that keyword arguments must be strings
d = dict(four = 4, five = 5)
d2 = dict(one = 1, two = 2, three = 3, **d)
print(d2)
# Creating an empty dictionary
empty_dictionary = dict()
print("%r is an empty dictionary" % empty_dictionary)
empty_dictionary = {}
print("%r is an empty dictionary" % empty_dictionary)
# Creating a dictionary
dictionary = {1:True, 0:False}
print("%r is a dictionary" % dictionary)
my_dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("%r is a dictionary" % my_dictionary)
# Creating a dictionary from a list of 2-tuples
list_two_tuples = [(1, 'x'), (2, 'y'), (3, 'z')]
print("The list of two tuples is %r" % list_two_tuples)
dictionary = dict(list_two_tuples)
print("The dictionary is %r" % dictionary)
# Creating a dictionary using a zip object
zipObj = zip(range(1, 101), ["One", "Two", "Three", "Four", "Five"])
print("The zip object is %r" % zipObj)
dictionary = dict(zipObj)
print("The dictionary is %r" % dictionary)
# Creating a dictionary from another dictionary using dict function
dictionary1 = {"One":1, "Two":2, "Three":3}
print("The first dictionary is %r" % dictionary1)
dictionary2 = dict(dictionary1)
print("The second dictionary is %r" % dictionary2)
print("Is the first dictionary %r == the second dictionary %r? %r" % (dictionary1, dictionary2, dictionary1 == dictionary2))
print("Is the first dictoinary %r is the second dictionary %r? %r" % (dictionary1, dictionary2, dictionary1 is dictionary2))
# dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.
dictionary = dict(one = 1, Two = 2) 	# one and two are interpreted as strings not variables
print("The dictionary is %r" % dictionary)
print(dictionary['one'], dictionary['Two'])
print("The type of the keys:")
for i in dictionary.keys():
    print(type(i))
# Printing a dictionary ordered with keys
d = {"one":1, "two":2, "three":3, "four":4, "five":5}
print(d, "is the dictionary")
print("The elements of the dictionary as 2-tuples ordered by keys are:")
for k in sorted(d.keys()):
    print(k, d[k])
d = dict(
    one = 1, two = 2, three = 3, four = 4, five = 'five'
)
print(d, "is the dictionary")
print("The elements of the dictionary as 2-tuples ordered by keys are:")
for k in sorted(d.keys()):
    print(k, d[k])
# Creating a dictionary from a list of strings of size two
l = ["ab", "bc", "de"]
print("Creating a dictionary from the list %r which contains strings of size two" % l)
dictionary = dict(l)
print("The dictionary is %r" % dictionary)
# Deleting a key-value pair using the del operator
dictionary = {1:True, 0:False}
print("The dictionary is %r, deleting the key 1, we have:" % dictionary)
del dictionary[1]
print(dictionary)
# Intializing a dictionary using a for loop and a list of 2-tuples
list_of_two_tuples = [(1, 2), (3, 4), (True, False)]
print("The list of two tuples is %r" % list_of_two_tuples)
dictionary = {}
print("%r is an empty dictionary" % dictionary)
for k, v in list_of_two_tuples:
    dictionary[k] = v
print("The dictionary is %r" % dictionary)
# Accessing the value of a specific key in a dictionary
my_dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % my_dictionary)
print("The value of the key \"One\" is %d" % my_dictionary["One"])
# Accessing the values of the keys of a dictionary using a for loop with the dict.values() function
print("The values of the dictionary are:")
for v in my_dictionary.values():
    print(v)
# Accessing the keys of a dictionary using a for loop with the dict.keys() function
print("The keys of the dictionary are:")
for k in my_dictionary.keys():
    print(k)
# Reassigning the value of a specific key in a dictionary
dictionary = {"Mohamed":"CEO", "Ali":"CTO"}
print("The dictionary is %r" % dictionary)
print("Changing the value associated with the key \"Mohamed\":")
dictionary["Mohamed"] = "Manager"
print("The dictionary now is %r" % dictionary)
# in operator works fine for checking for the existance of a key in a dictionary
print("The dictionary is %r" % dictionary)
print("\"Mohamed\" in %r? %r" % (dictionary, "Mohamed" in dictionary))
print("\"mohamed\" in %r? %r" % (dictionary, "mohamed" in dictionary))
print("\"hussin\" in %r? %r" % (dictionary, "hussin" in dictionary))
# in operator and checking for the existance of a value
print("The dictionary is %r and its values are %r" % (dictionary, dictionary.values()))
print("\"CEO\" in %r? %r" % (dictionary.values(), "CEO" in dictionary.values()))
print("\"Manager\" in %r? %r" % (dictionary.values(), "Manager" in dictionary.values()))
# in operator and checking for the existance of a key-value pair
print("The dictionary is %r and its key-value pairs are %r" % (dictionary, dictionary.items()))
print("The key-value pair (\"Mohamed\", \"Manager\") in %r? %r" % (dictionary.items(), ("Mohamed", "Manager") in dictionary.items()))
print("The key-value pair (\"Mohamed\", \"CEO\") in %r? %r" % (dictionary.items(), ("Mohamed", "CEO") in dictionary.items()))
# Inserting items to a dictionary
dictionary = {5:"Five", 6:"Six", 2:"Two"}
print("The dicitonary is %r" % dictionary)
if 1 in dictionary:    pass
else:    dictionary[1] = "One"
if 3 in dictionary:    pass
else:    dictionary[3] = "Three"
if 4 in dictionary:    pass
else:    dictionary[4] = "Four"
if 2 in dictionary:    pass
else:    dictionary[2] = "Two"
print("The dictionary now is %r" % dictionary)
# for loops traverses the keys of the dictionary
print("The key-value pairs of the dictionary are:")
for k in dictionary:
    print("(%d, %s)" % (k, dictionary[k]), end = ' ')
print("")
print("The key-value pairs of the dictionary are:")
for k, v in dictionary.items():
    print("(%d, %s)" % (k, v), end = ' ')
print('')
# Reverse lookup
print("The dictionary is %r" % dictionary)
print("The keys their values are \"One\" or \"Two\" are:")
for k in dictionary:
    if dictionary[k] == "One" or dictionary[k] == "Two":
        print(k, end = ' ')
print("")
new_dict = dict(one = 1, two = 2, three = 3)
new_dict2 = dict(four = 4, five = 5, six = 6)
new_dict3 = dict(four = 4, five = 5, six = 6, **new_dict)
print(new_dict)
print(new_dict2)
print(new_dict3)
del new_dict3['four']
print(new_dict3)

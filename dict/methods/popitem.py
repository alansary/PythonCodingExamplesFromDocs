# popitem()
'''
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
'''
	# The key-value pair that will be popped is unpredictable
dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % dictionary)
print("Popping a random item from the dictionary")
popped = dictionary.popitem()
print("The dicitionary now is %r and the popped key value-pair is %r" % (dictionary, popped))
print("Popping a random item from the dictionary")
popped = dictionary.popitem()
print("The dicitionary now is %r and the popped key-value pair is %r" % (dictionary, popped))
print("Popping a random item from the dictionary")
popped = dictionary.popitem()
print("The dicitionary now is %r and the popped key-value pair is %r" % (dictionary, popped))
print("Popping a random item from the dictionary")
popped = dictionary.popitem()
print("The dicitionary now is %r and the popped key-value pair is %r" % (dictionary, popped))
print("Popping a random item from the dictionary")
popped = dictionary.popitem()
print("The dicitionary now is %r and the popped key-value pair is %r" % (dictionary, popped))
print("Popping a random item from the dictionary")
popped = dictionary.popitem()
print("The dicitionary now is %r and the popped key-value pair is %r" % (dictionary, popped))
print("Popping a random item from the dictionary")
popped = dictionary.popitem()
print("The dicitionary now is %r and the popped key-value pair is %r" % (dictionary, popped))
print("If the dictionary is empty and we tryied to pop an item from the dictionary, it will raise a KeyErro")
print("We can handle such an erro by checking len(dict) before popping an item")
if len(dictionary) > 0:
    print("Popping a random item from the dictionary")
    popped = dictionary.popitem()
    print("The dictionary now is %r and the popped key-value pair is %r" % (dictionary, popped))
else:
    print("The dictionary is empty, we can not pop an item from an empty dictionary")
print("We will try to pop from an empty dictionary without handling the error and see what happens")
print("Popping a random item from the dictionary")
popped = dictionary.popitem()


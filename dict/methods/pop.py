# pop()
'''
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
'''
dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % dictionary)
print("Popping the key \"Initial-list\", we have:")
popped = dictionary.pop("Initial-list")
print("The value associated with the popped key is %r and the dictionary now is %r" % (popped, dictionary))
print("Is \"Mohamed\" in %r? %r" % (dictionary, "Mohamed" in dictionary))
print("Trying to pop a non existance key \"Mohamed\" and returning -1 on faliure")
popped = dictionary.pop("Mohamed", -1)
if popped == -1:
    print("The key doesn't exist in the dictionary %r and %d is returned" % (dictionary, popped))
else:
    print("The value associated with the popped key is %r and the dictioanry now is %r" % (popped, dictioanry))
to_pop = input("Enter a key to pop:")
key = None
for k in dictionary.keys():
    if str(k) == to_pop:
        key = k
if not key == None:
    popped = dictionary.pop(key)
    print("The key %r is now popped of the dictioanry %r and its associated value is %r" % (key, dictionary, popped))
if key == None:
    print("The key you are trying to pop doesn't exist in the dictionary")
print("We can check for the existance of a key using the in operator")
print("Adding a new key-value pair ('n', 'x') to the dictionary")
dictionary['n'] = 'x'
print("The dictionary now is %r" % dictionary)
print("Popping this key-value pair")
if 'n' in dictionary.keys():
    popped = dictionary.pop('n')
    print("The value associated with the popped key %s is %s and the dictionary now is %r" % ('n', popped, dictionary))
else:
    print("The key doesn't exist in the dictionary")
print("Trying to pop a key that doesn't exist without returning a default return value, and KeyError will raise")
popped = dictionary.pop('ans')


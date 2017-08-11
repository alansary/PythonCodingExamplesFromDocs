# clear()
'''
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
'''
my_dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % my_dictionary)
print("Clearing the dictioanry...")
my_dictionary.clear()
print("The dictionary now is %r" % my_dictionary)


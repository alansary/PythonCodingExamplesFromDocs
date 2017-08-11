# items()
'''
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
'''
my_dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % my_dictionary)
print("The key-value pairs (items) of the dictionary are %r" % my_dictionary.items())
print("The key-value pairs (items) of the dictionary are:")
for i in my_dictionary.items():
    print(i, end = ' ')
print("")


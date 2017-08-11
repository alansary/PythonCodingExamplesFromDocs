# copy()
'''
 |  copy(...)
 |      D.copy() -> a shallow copy of D
'''
print("Copying the first dictionary to the second dictionary using the copy method")
dictionary1 = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The first dictionary is %r" % dictionary1)
dictionary2 = dictionary1.copy()
print("The second dictionary is %r" % dictionary2)
print("Is the first dictionary == the second dictionary? %r" % (dictionary1 == dictionary2))
print("Is the first dictionary is the second dictioanry? %r" % (dictionary1 is dictionary2))
print("Creating the third dictionary and initializing it from the first dictionary")
dictionary3 = dict(dictionary1)
print("The third dictionary is %r" % dictionary3)
print("Is the first dictionary == the third dictionary? %r" % (dictionary1 == dictionary3))
print("Is the first dictioanry is the third dictioanry? %r" % (dictionary1 is dictionary3))
print("Creating the fourth dictionary with the same key-value pairs as the first dictionary")
dictionary4 = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The fourth dictionary is %r" % dictionary4)
print("Is the first dictionary == the fourth dictioanry? %r" % (dictionary1 == dictionary4))
print("Is the first dictionary is the fourth dictioanry? %r" % (dictionary1 is dictionary4))
print("Assigning the first dictioanry to the fifth dictionary")
dictionary5 = dictionary1
print("The fifth dictionary is %r" % dictionary5)
print("Is the first dictionary == the fifth dictionary? %r" % (dictionary1 == dictionary5))
print("Is the first dictionary is the fifth dictioanry? %r" % (dictionary1 is dictionary5))
print("Making a change to the first dictionary (i.e., clear()) will affect only the fifth dictionary (Aliasing)")
print("Clearing the first dictionanry...")
dictionary1.clear()
print("The first dictionary is %r" % dictionary1)
print("The second dictionary is %r" % dictionary2)
print("The third dictionary is %r" % dictionary3)
print("The fourth dictionary is %r" % dictionary4)
print("The fifth dictionary is %r" % dictionary5)


# setdefault()
'''
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
'''
	# If it does exist, it will return its associated value.
	# If it doesn't exist, it will be appended.
dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % dictionary)
print("setdefault(\"Initial-list\") returns %r" % dictionary.setdefault("Initial-list"))
print("setdefault(\"Initial-list\", 'x') returns %r" % dictionary.setdefault("Initial-list"))
print("The dictionary now is %r (still the same)" % dictionary)
print("setdefault(True) appends the key True in the dictionary and associate the value None with it")
dictionary.setdefault(True)
print("The dictionary now is %r" % dictionary)
print("setdefault(\"Alansary\", 'ans') appends the key \"Alansary\" in the dictionary and associate the value 'ans' with it")
dictionary.setdefault("Alansary", 'ans')
print("The dictionary now is %r" % dictionary)


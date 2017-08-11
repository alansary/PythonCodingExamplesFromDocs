# get()
'''
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
'''
dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % dictionary)
print("Getting the value of the key \"Initial-list\": %r" % dictionary.get("Initial-list"))
print("Getting the value of a non-existance key, say, \"Hi\": %r" % dictionary.get("Hi"))
print("Getting the value of a non-existance key, say, \"Hi\" and returning -1 on faliure: %d" % dictionary.get("Hi", -1))


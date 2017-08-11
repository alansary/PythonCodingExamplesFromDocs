# values()
'''
 |  values(...)
 |      D.values() -> an object providing a view on D's values
'''
my_dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % my_dictionary)
print("The values of the dictionary are %r" % my_dictionary.values())
print("The values of the dictionary are:")
for v in my_dictionary.values():
    print(v, end = ' ')
print("")
print("The keys of the dictionary are:")
for v in my_dictionary.values():
    for k in my_dictionary.keys():
        if my_dictionary[k] == v:
            print(k, end = ' ')
        else:
            pass
print("")
print("The key-value pairs of the dictionary are:")
key_value = []
for v in my_dictionary.values():
    for k in my_dictionary.keys():
        if my_dictionary[k] == v:
            if not (k, v) in key_value:
                key_value.append((k, v))
for i in key_value:
    print(i, end = ' ')
print("")


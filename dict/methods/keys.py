# keys()
'''
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
'''
my_dictionary = {"One":1, "Zero":False, False:0, "Initial-list":[0, 1], (0, 1):"Initial-tuple", "Proposition":{True:1, False:0}, 3.2:"3.2", "F":False}
print("The dictionary is %r" % my_dictionary)
print("The keys of the dictionary are %r" % my_dictionary.keys())
print("The keys of the dictionary are:")
for k in my_dictionary.keys():
    print(k, end = ' ')
print("")
print("The values of the dictionary are:")
for k in my_dictionary.keys():
    print(my_dictionary[k], end = " ")
print(' ')
print("The key-value pairs of the dictionary are:")
for k in my_dictionary.keys():
    print("(%r, %r)" % (k, my_dictionary[k]), end = ' ')
print(' ')


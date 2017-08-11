'''
repr(...)
    repr(object) -> string
    
    Return the canonical string representation of the object.
    For most object types, eval(repr(object)) == object.
'''
my_dictionary = {True:1, False:0}
print("The dictionary is %r" % my_dictionary)
print("The raw representation of the dictionary is", repr(my_dictionary))


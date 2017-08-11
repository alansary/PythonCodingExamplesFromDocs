test_dict = {}
print("The dictionary is %r" % test_dict)
string = "This is a string"
print("The string is %s, mapping each character to its number of occurrences in the string within the dictionary, we have:" % string)
test_dict = {character:string.count(character) for character in string}
print("The dictionary now is %r"  % test_dict)
test_dict = {}
print("The dictionary is %r" % test_dict)
test_set = set("This is a string")
print("The set is %r, mapping each element in the set to its number of occurrences in the set within the dictionary, we have:" % test_set)
test_dict = {element:str(test_set).count(element) for element in test_set}
print("The dictionary now is %r" % test_dict)


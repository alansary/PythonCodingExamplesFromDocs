test_string = "This is a string000@1"
print("The string is %s, the characters of the string are:" % test_string)
for c in test_string:
    print(c, end = ' ')
print("")
test_list = [1, 1.5, True, {1:True, 0:False}, (1, 2), {1, 2, 3}, "string"]
print("The list is %r, the elements of the list are:" % test_list)
for e in test_list:
    print(e, end = ' ')
print("")
test_dict = {1:"One", 1.5:"ThreeHalfs", "Two":2, False:0, (1, 2, 3):"Tuple"}
print("The dictionary is %r, the keys of the dictionary are:" % test_dict)
for key in test_dict:
    print(key, end = ' ')
print("\nThe keys of the dictionary are:")
for key in test_dict.keys():
    print(key, end = ' ')
print("\nThe values of the dictionary are:")
for value in test_dict.values():
    print(value, end = ' ')
print("\nThe items of the dictionary are:")
for item in test_dict.items():
    print(item, end = ' ')
print("\n the keys and values of the dictionary are:")
for key, value in test_dict.items():
    print(key, value)
print("\n")
list_of_two_tuples = [('M', 'Mohamed'), (1, True), (0, False)]
print("The list of two tuples is %r, the elements of the list of two tuples are:" % list_of_two_tuples)
for e1, e2 in list_of_two_tuples:
    print(e1, e2)
print("")
test_tuple = (1, 1.5, [1, 2], {1:True, 0:False}, False, {1, 2}, "string")
print("The tuple is %r, the elements of the tuple are:" % (test_tuple,))
for e in test_tuple:
    print(e, end = ' ' )
print("")
test_set = {1, 1.5, False, "string"}
print("The set is %r, the members of the set are:" % test_set)
for member in test_set:
    print(member, end = ' ')
print("")
test_rangeObj = range(1, 10, 2)
print("The range object is %r, the elements of the range object are:" % test_rangeObj)
for e in test_rangeObj:
    print(e, end = ' ')
print("")
test_zipObj = zip(range(1, 10), "This is a string", ['x', 'y', 'z', False, True, "string", 'a', 'b', 'c', {1, 2}, (1, 2), {1:True, False:0}])
print("The zip object is %r, the elements of the zip object are:")
for e1, e2, e3 in test_zipObj:
    print(e1, e2, e3)
print("")
test_string = "This is a string"
print("The string is %s, looping through the indices of this string" % test_string)
print("The indices and its associated values are:")
for i in range(0, len(test_string), 1):
    print("The character '%s' is in the index %d" % (test_string[i], i))
print("")


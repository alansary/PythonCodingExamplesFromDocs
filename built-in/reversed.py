# reversed()
'''
Help on class reversed in module builtins:

class reversed(object)
 |  reversed(sequence) -> reverse iterator over values of the sequence
 |  
 |  Return a reverse iterator
'''
test_string = "This is a sting"
test_string_reverse_iterator = reversed(test_string)
test_list = ['one', 'two', 'three']
test_list_reverse_iterator = reversed(test_list)
test_tuple = (1, 2, 3)
test_tuple_reverse_iterator = reversed(test_tuple)
test_rangeObj = range(1, 11)
test_rangeObj_reverse_iterator = reversed(test_rangeObj)
print("The list of the iterator %r is %r" % (test_string_reverse_iterator, list(test_string_reverse_iterator)))
print("The list of the iterator %r is %r" % (test_list_reverse_iterator, list(test_list_reverse_iterator)))
print("The list of the iterator %r is %r" % (test_tuple_reverse_iterator, list(test_tuple_reverse_iterator)))
print("The list of the iterator %r is %r" % (test_rangeObj_reverse_iterator, list(test_rangeObj_reverse_iterator)))
# Note that range is a sequence

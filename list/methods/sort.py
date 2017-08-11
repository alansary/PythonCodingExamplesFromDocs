# sort()
'''
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
'''
	# This method sorts the list in place, using only < comparisons between items.
	# key specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower).
	# The key corresponding to each item in the list is calculated once and then used for the entire sorting process.
	# The default value of None means that list items are sorted directly without calculating a separate key value.
	# reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
shopping_list = ['computer', 'labtop', 'mouse', 'keyboard', 'pad', 'screen', 'printer', 'scanner', 'network lan', 'wireless lan']
print("The shopping list is %r" % shopping_list)
shopping_list.sort()
print("Sorting the shopping list in place, we have: %r" % shopping_list)
shopping_list = ['computer', 'labtop', 'mouse', 'keyboard', 'pad', 'screen', 'printer', 'scanner', 'network lan', 'wireless lan']
print("The shopping list is %r (Original State Again)" % shopping_list)
shopping_list.sort(key = None, reverse = True)
print("Sorting and reversing the shopping list in place, we have: %r" % shopping_list)
shopping_list = ['computer', 'labtop', 'mouse', 'keyboard', 'pad', 'screen', 'printer', 'scanner', 'network lan', 'wireless lan']
print("The shopping list is %r (Original State Again)" % shopping_list)
shopping_list.sort(key = None, reverse = False)
print("Sorting and (Not reversing) the shopping list in place, we have: %r" % shopping_list)
shopping_list = ['computer', 'labtop', 'mouse', 'keyboard', 'pad', 'screen', 'printer', 'scanner', 'network lan', 'wireless lan']
shopping_list.sort(key = str.lower, reverse = False)
print("Sorting the shopping list with key 'str.lower' and 'reverse = False', we have: %r" % shopping_list)


# count()
'''
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
'''
	# Note that: count takes value and only value as an argument (not like count with strings that takes sub-string,
	# start, and end as arguments)
my_list = [1, 2, 3, 2, 1, 1, 4, 7, 2, 1, 8, 7]
print("The list is %r" % my_list)
print("The number of occurrences of the value 1 in %r is %d" % (my_list, my_list.count(1)))
print("The number of occurrences of the value 1 in the sub-list %r is %d" % (my_list[4:], my_list[4:].count(1)))


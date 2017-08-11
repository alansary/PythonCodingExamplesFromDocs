# index()
'''
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
'''
t = (1, 2, 1, 1, 3, 4, 2, 3, 5, 4)
print("The tuple is %r" % (t,))
print("The first index of '1' in the tuple is %d" % t.index(1))
print("The first index of '3' in the tuple is %d" % t.index(3))
print("Trying to find the index of an item that doesn't exist in the tuple will raise a ValueError")
if 0 in t:
    print("The first index of '0' in the tuple is %d" % t.index(0))
else:
    print("'0' doesn't exist in the tuple, trying to find the index of it will raise a ValueError")
item = int(input("Enter a value in the tuple to get its index (If the value doesn't exist, it will raise a ValueError):"))
print("The index of %d in the tuple %r is %d" % (item, t, t.index(item)))


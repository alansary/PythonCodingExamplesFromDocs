# insert()
'''
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
'''
        # If you want to insert the element in index > len(L) it will assume that index = len(l)
shopping_list = ['computer', 'mouse', 'keyboard']
print("The shopping list is %r" % shopping_list)
shopping_list.insert(0, 'labtop')
print("Inserting 'labtop' in index 0, we have: %r" % shopping_list)
shopping_list.insert(2, 'pad')
print("Inserting 'pad' in index 2, we have: %r" % shopping_list)
shopping_list.insert(5, 'microphone')
print("Inserting 'microphone' in index 5, we have: %r" % shopping_list)
shopping_list.insert(100, 'ipod')
print("Inserting 'ipod' in index 100 which is greater than the length of the shopping list, it will insert it at index len(L), we have: %r" % shopping_list)


# del list_slice
shopping_list = ['computer', 'labtop', 'mouse', 'keyboard', 'screen', 'touch', 'pad', 'printer', 'scanner']
print("The shopping list is %r" % shopping_list)
print("Deleting the item in index 4, we have:")
del shopping_list[4]
print(shopping_list)
print("Deleting the items from index 2 up to but not including index 5, we have:")
del shopping_list[2:5]
print(shopping_list)
print("Deleting all the items in the shopping list, we have:")
del shopping_list[:]
print(shopping_list)


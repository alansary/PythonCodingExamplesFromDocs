# remove()
'''
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
'''
	# Note: If an element exists more than once, it will remove the first occurrence of this item.
shopping_list = ['computer', 'labtop', 'mouse', 'computer', 'keyboard']
print("The shopping list is %r" % shopping_list)
print("Removing 'labtop' from the list, we have:")
if 'labtop' in shopping_list:
    shopping_list.remove('labtop')
    print(shopping_list)
else:
    print("'labtop' doesn't exist in the shopping list")
print("Trying to remove a value that doesn't exist in the list will raise a ValueError")
while True:
    if len(shopping_list) == 0:
        print("The shopping list is empty, trying to remove any item will raise a ValueError")
        item = input("Enter an item to remove (It will raise a ValueError):")
        shopping_list.remove(item)
    else:
        item = input("Enter an item to remove:")
        if item in shopping_list:
            shopping_list.remove(item)
            print(shopping_list)
        else:
            print("The item doesn't exist in the list, removing it will raise a ValueError")


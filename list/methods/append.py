# append()
'''
 |  append(...)
 |      L.append(object) -> None -- append object to end
'''
shopping_list = ['computer', 'mouse']
print("My shopping list is %r" % (shopping_list))
clothes = ['socks', 'shoes', 't-shirts']
print("Appending labtop and keyboard and the list %r to my shopping list" % clothes)
shopping_list.append('labtop')
shopping_list.append('keyboard')
shopping_list.append(clothes)
print("My shopping list now is %r" % shopping_list)
shopping_list.append(input("Enter an item to append to the list: "))
print("My shopping list now is", shopping_list)
shopping_list.append(int(input("Enter the total price to append to the list: ")))
print("My shopping list now is", shopping_list)

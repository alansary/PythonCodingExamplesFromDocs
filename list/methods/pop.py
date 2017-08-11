# pop()
'''
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
'''
shopping_list = ['computer', 'labtop', 'mouse', 'keyboard', 'screen', 'microphone']
print("The shopping list is %r" % shopping_list)
print("Popping the element at the end, we have:")
shopping_list.pop()
print(shopping_list)
print("Popping the element at index 2, we have:")
shopping_list.pop(2)
print(shopping_list)
print("Popping the first element, we have:")
shopping_list.pop(0)
print(shopping_list)
print("Trying to pop from an index which is out of range or popping from an empty list raises an IndexError")
ans = "y"
while ans == "y":
    ans = input("Do you want to pop an item of the list %r\t(Y/N)\n" % shopping_list).lower()
    if ans == 'y':
        if len(shopping_list) > 0:
            index = None
            while True:
                try:
                    index = int(input("Enter an index:"))
                    if(len(shopping_list) <= index):
                        print("IndexError (index out of range), max-index = %d" % (len(shopping_list)-1))
                    else:
                        print("The popped element is %s and the list now is %r" %(shopping_list.pop(index), shopping_list))
                        break
                except:
                    print("Please, enter a valid index")
        else:
            print("You can not pop since the list is empty %r" % shopping_list)
            break
    else:
        break


# copy()
'''
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
'''
list1 = ['socks', 't-shirts', 'shoes']
print("The first list is %r, copying it to list2" % list1)
list2 = list1.copy()
print("The second list is %r" % list2)
print("Is the first list == the second list? %r (They are equivalent)" % (list1 == list2))
print("Is the first list is the second list? %r (They are identical)" % (list1 is list2))
list3 = [1, 2, 3]
list4 = [1, 2, 3]
print("We assigned the third list the value %r and the fourth list the value %r" % (list3, list4))
print("Is the third list == the fourth list? %r (They are equivalent)" % (list3 == list4))
print("Is the third list is the fourth list? %r (They are identical)" % (list3 is list4))
list5 = [1, 2, 3]
list6 = list5[:]
print("We assigned the fifth list the value %r and assigned the sixth list the value of the fifth list by using the slice operator" % list5)
print("The sixth list is %r" % list6)
print("Is the fifth list == the sixth list? %r (They are equivalent)" % (list5 == list6))
print("Is the fifth list is the sixth list? %r (They are identical)" % (list5 is list6))
list7 = [1, 2, 3]
list8 = list7
print("We assigned the seventh list the value %r and assigned the eights list the value of the seventh list without using slicing" % list7)
print("The eights list is %r" % list8)
print("Is the seventh list == the eights list? %r (They are equivalent)" % (list7 == list8))
print("Is the seventh list is the eights list? %r (They are identical)" % (list7 is list8))


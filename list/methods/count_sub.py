# count_sub()
'''
 |  count_sub(...)
 |      L.count_sub(l, sub_list, start_index, end_index) -> integer -- return number of occurrences of sub_list in L
'''
def count_sub(l, sub_list, start_index, end_index):
    if len(sub_list) == 1:
        return l.count(sub_list[0])
    else:
        # Calculating the indics in l of each element and saving them within temp_list_final
        temp_list_final = list() # temp_list_final holds the lists of indices in l of each element in the sub_list
        for element in sub_list:
            temp_list = list() # temp_list holds temporarily the indices in l of the element in the sub_list
            si, ei = start_index, end_index # si and ei are the new indices
            try:
                l[start_index:end_index].index(element) # Trying to find the element in l at the first time
                temp_list.append(l[start_index:end_index].index(element) + start_index) # If it exists append its index in the temp_list
                si = l[start_index:end_index].index(element) + 1 # si is the new index at which we start our loop
                while si != ei: # while there are elements in the l[si:ei] (l[si:ei] is not empty)
                    try:
                        l[si:ei].index(element) # Search from the new index to the end index for the element
                        temp_list.append(l[si:ei].index(element) + si) # If it exists append the index in l to the temp_list
                        si += l[si:ei].index(element) + 1 # Incrementing si by (the index we found + 1)
                    except: break # If the element doesn't exist any more in l
            except:
                return 0 # The element doesn't exist in l
            temp_list_final.append(temp_list)
        # Saving all indices we get as ordered elements in straight_forward_list1
        straight_forward_list1 = list()
        for x in temp_list_final:
            for y in x:
                straight_forward_list1.append(y)
        straight_forward_list1.sort()
        # Removing duplicates in straight_forward_list1 and creating the final list, straight_forward_list
        straight_forward_list = list()
        for element in straight_forward_list1:
            if element in straight_forward_list: pass
            else: straight_forward_list.append(element)
        # Checking the straight_forward_list for "len(sub_list)" consecutive indices, if it exists append it to consecutive_list
        consecutive_list = list()
        for x in straight_forward_list: # Looping throgh the indices
            consecutive_list_sub = list() # Temporarily holding the consecutive indices
            consecutive_list_sub.append(x)
            counter = 0 # Counts the number of consecutive numbers to x
            i = 1 # The iterator of the next indices to x and the increment value for x at each step
            if straight_forward_list.index(x)+i < len(straight_forward_list) and x + i == straight_forward_list[straight_forward_list.index(x) + i]:
                consecutive_list_sub.append(straight_forward_list[straight_forward_list.index(x)+i]) # Append the next index if it is consecutive to x
                counter += 1 # Increment the counter of the number of consecutive indices
                while len(consecutive_list_sub) != len(sub_list): # Checking whether we have "len(sub_list)" consecutive indices
                    i += 1 # Increment i to compare the next index
                    if straight_forward_list.index(x)+i < len(straight_forward_list) and x + i == straight_forward_list[straight_forward_list.index(x) + i]:
                        consecutive_list_sub.append(straight_forward_list[straight_forward_list.index(x)+i])
                        counter += 1 # Increment the counter if the index is consecutive to the previous one
                    else:
                        counter = 0 # That means we failed to find "len(sub_list)" consecutive indices, starting with the index x
                        break
                if not (counter == 0):
                    consecutive_list.append(consecutive_list_sub) # If we found "len(sub_list)" consecutive indices, append them to consecutive_list
            else:
                pass
        # Check each list in consecutive_list
        counter = 0 # Counts the final number of occurences of the sub_list in l
        for x in consecutive_list:
            match = None
            for i in range(len(x)):
                if sub_list[i] == l[x[i]]: # Looping through sub_list and l
                    match = True
                else:
                    match = False
                    break
            if match == True: counter += 1
        return counter # Return the final count
l = [1, 2, 4, 5, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6]
sub_list = [4, 5, 6]
print("The number of occurrences of the sub_list %r in the list %r is %d" % (sub_list, l, count_sub(l, sub_list, 0, len(l))))
sub_list = []
print("The number of occurrences of the sub_list %r in the list %r is %d" % (sub_list, l, count_sub(l, sub_list, 0, len(l))))
sub_list = [1, 2, 3]
print("The number of occurrences of the sub_list %r in the list %r is %d" % (sub_list, l, count_sub(l, sub_list, 0, len(l))))
sub_list = [4]
print("The number of occurrences of the sub_list %r in the list %r is %d" % (sub_list, l, count_sub(l, sub_list, 0, len(l))))
sub_list = [3, 4]
print("The number of occurrences of the sub_list %r in the list %r is %d" % (sub_list, l, count_sub(l, sub_list, 0, len(l))))
sub_list = [4, 5, 6]
print("The number of occurrences of the sub_list %r in the list %r, searching from index 5 to the end is %d" % (sub_list, l, count_sub(l, sub_list, 5, len(l))))
print("The number of occurrences of the sub_list %r in the list %r, searching from index 6 to the end is %d" % (sub_list, l, count_sub(l, sub_list, 6, len(l))))
print("The number of occurrences of the sub_list %r in the list %r, searching from index 5 to index 8, not including index 8 is %d" % (sub_list, l, count_sub(l, sub_list, 5, 8)))


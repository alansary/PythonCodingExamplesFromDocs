# reverse()
'''
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
'''
shopping_list = ['computer', 'mouse', 'keyboard', 'pad', 'screen', 'microphone']
print("The shopping list is %r" % shopping_list)
shopping_list.reverse()
print("The shopping list is now reversed, it is %r" % shopping_list)
shopping_list = shopping_list[::-1]
print("The shopping list is now reversed, it is %r" % shopping_list)
line = input("Enter a line of text to reverse:")
# Reversing a line of text
print("You input: %s" % line)
line_list = line.split(' ') # Split the line into words
line_list.reverse() # Reverse the order of words
print("The reverse of the line (reversing each character) is %s" % line_list)
counter = 0
for x in line_list: # Loop through the words
    temp_list = list(x) # List each word as characters
    temp_list.reverse() # Reverse each word as characters
    word_reversed = ''.join(temp_list) # Join the reversed characters
    line_list[counter] = word_reversed # Replace each word by the reversed word
    counter += 1
line_reversed = ' '.join(line_list) # Join the reversed list of words that contain all reversed words as a reversed line
print("The reverse of the line (reversing each character) is %s" % line_reversed)
print("The reverse of the line (reversing each character) is %s" % line[::-1])


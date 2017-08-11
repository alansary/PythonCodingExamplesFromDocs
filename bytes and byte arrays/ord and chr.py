#!/usr/bin/env python3
# utf_8 contains all ascii from 0-127
# ord(char) & chr(ord)



def main():
    # Creating a dictionary with keys as the ordinals and values as the characters (ascii table)
    dictionary = {}
    for i in range(0, 128):
        dictionary[i] = chr(i)
    # listing the dictionary in a list of 2-tuples and sort them with ordinals
    l = []
    for item in dictionary.items():
        l.append(item)
    l.sort()
    print(l)
    # Creating a file and writing ascii table into it
    fin = open('ascii.txt', 'w')
    ascii_string = ''
    for ordinal, character in l:
        ascii_string += character
    print(ascii_string, file = fin)

    # Opening the file ascii and reading the data into it
    fin = open('ascii.txt', 'r', encoding = 'utf_8')
    # Creating the bytearray to store the characters and fout object to write data in
    charbytearray = bytearray()
    fout = open('ascii.html', 'w', encoding = 'utf_8')
    # Looping through the file
    for line in fin:
        for char in line:
            if ord(char) > 127:
                charbytearray += bytes('&#{:04d};'.format(ord(char)), encoding = 'utf_8')
            else:
                charbytearray.append(ord(char))
    # Now, charbytearray contains all the characters in which any character out of ascii characters is converted to
    # utf-16 which is the normal unicode (all ascii are unicode characters, we don't have to convert them)
    # All encoded with the unicode XML entities

    # Turning the bytearray into a string
    final_string = str(charbytearray, encoding = 'utf_8')
    # Print the result on the screen and to the html file
    print(final_string)
    print(final_string, file = fout)

if __name__ == "__main__": main()
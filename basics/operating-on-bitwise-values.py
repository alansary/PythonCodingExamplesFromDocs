#!/usr/bin/env python3


def main():
    # Bitwise Operators (works with binary values)
    def b(n): return "{:08b}".format(n) # returns the binary value to eight places
    # return "{:0yb}.format(n) returns the binary value to y places
    x = 0b11010000011111011010111110 # initializing x as a binary value
    print(x, bin(x), hex(x), oct(x), int(x), float(x), str(x), repr(x))
    print(int(oct(x), 8), type(int(oct(x), 8)))
    print(b(5))
    print(b(54654654))
    x, y = 0x55, 0xaa # initializing x and y as hex values
    print("x =", b(x))
    print("y =", b(y))
    print("x or y =", b(x | y)) # This vertical bar is the or operator (inclusive or)
    print("x and y =", b(x & y)) # This ampersand is the and operator
    print("x exclusive or y =", b(x ^ y)) # This caret is the exclusive or
    print("x exclusive or 0 =", b(x ^ 0))
    print("x exclusive or 0xff =", b(x ^ 0xff))
    print("0xff =", b(0xff))

    print("The complement of x =", b(~x)) # This tilda is the complement operator
    # since it operates on the word size of the implementation which is more than eight bits I'm printing, it gets
    # assigned extension and it ends up look like that

    print("x left shifted by four bits =", b(x << 4)) # This is left-shift operator
    print("x right shifted by four bits =", b(x >> 4)) # This is right-shift operator
    '''
    Left Shift
    x = x * 2 ** value (Mathematically, normal arithmetic operation)
    x << value (bit-wise operation)
    Right Shift
    x = x // 2 ** value (Mathematically. normal arithmetic operation)
    x >> value (bit-wise operation)
    '''
    '''
    Summary:
        # If we encounter a leading 1 when left-shifting, we just append a zero at the right leaving every thing as it is
        # right-shift is removing a bit from the right and appending 0 to the left
    '''
    print(x, b(x))
    print(x << 1, b(x << 1), x * 2 ** 1, b(x * 2 ** 1))
    print(x << 2, b(x << 2), x * 2 ** 2, b(x * 2 ** 2))
    print(x << 3, b(x << 3), x * 2 ** 3, b(x * 2 ** 3))
    print(x << 4, b(x << 4), x * 2 ** 4, b(x * 2 ** 4))
    print(x, b(x))
    print(x >> 1, b(x >> 1), int(x / 2 ** 1), b(int(x / 2 ** 1)))
    print(x >> 2, b(x >> 2), int(x / 2 ** 2), b(int(x / 2 ** 2)))
    print(x >> 3, b(x >> 3), int(x / 2 ** 3), b(int(x / 2 ** 3)))
    print(x >> 4, b(x >> 4), int(x / 2 ** 4), b(int(x / 2 ** 4)))
    print('\n' * 8)
    for i in range(0, 11):
        print("{} << {} is {}".format(b(x), i, b(x << i)))
        print("{} << {} is {}".format(x, i, (x << i)))
    print('\n' * 8)
    for i in range(0, 11):
        print("{} >> {} is {}".format(b(x), i, b(x >> i)))
        print("{} >> {} is {}".format(x, i, (x >> i)))
    print('\n' * 8)
    for i in range(0, 11):
        print("{} << {} is {}".format(b(0b11111110), i, b(0b11111110 << i)))
        print("{} << {} is {}".format(0b11111110, i, (0b11111110 << i)))
    print('\n' * 8)
    for i in range(0, 11):
        print("{} >> {} is {}".format(b(0b11111110), i, b(0b11111110 >> i)))
        print("{} >> {} is {}".format(0b11111110, i, (0b11111110 >> i)))
    print('\n' * 8)
    # Boolean Operators (works with bits)
    print(True and True)
    print(False and False)
    print(True and False)
    print(False and True)
    print(True or True)
    print(False or False)
    print(True or False)
    print(False or True)
    print(not True)
    print(not False)
if __name__=="__main__": main()

#!/usr/bin/env python3

def main():
    integer_var = 42
    float_var1, float_var2 = 42.0, 42.5
    print(integer_var, type(integer_var), id(integer_var))
    print(float_var1, type(float_var1), id(float_var1))
    print(float_var2, type(float_var2), id(float_var2))
    print("Division of 42 / 9 =", 42 / 9)
    print("Integer division (Truncated division) of 42 // 9 =", 42 // 9)
    print("The remainder of division of 42 / 9 =", 42 % 9)
    print("The division of 42 / 9 rounded to the nearest integer =", round(42 / 9))
    print("The division of 42 / 9 rounded to the second decimal place =", round(42 / 9, 2))
    x = 12.5
    print(x, type(x), id(x))
    x = int(12.5)
    print(x, type(x), id(x))
    y = 12
    print(y, type(y), id(y))
    y = float(12)
    print(y, type(y), id(y))
    # float and int are actually object constructors, i.e., y = float(x) creates an object y of the class float
    print(abs(-10), min([10, 12, 3]), max([10, 12, 3]), sum([10, 12, 3]), abs(10))
    print(min([sum([11, 22]), max(abs(-30), 2)]))
if __name__ == "__main__": main()
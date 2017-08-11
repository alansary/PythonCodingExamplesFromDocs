#!/usr/bin/env python
from addfun import addFun
import mulfun
from subfun import subfun
import divfun
def get_vars():
    x, y = None, None
    while True:
        x = input("Enter the first number [q = quit]:")
        if x == 'q': break
        try:
            x = float(x)
            while True:
                y = input("Enter the second number [q = quit]:")
                if y == 'q': break
                try:
                    y = float(y)
                    break
                except:
                    print("%r must be a float or an integer" % y)
            break
        except:
            print("%r must be a float or an integer" % x)
    return x, y
def calc(op):
    x, y = get_vars()
    if not x == 'q' and not y == 'q' and not x == None and not y == None:
        if op == '+': print("The summation of %f and %f is %f" % (x, y, addFun(x, y)))
        elif op == '*': print("The multiplication of %f and %f is %f" % (x, y, mulfun.mulFun(x, y)))
        elif op == '-': print("The subtraction of %f and %f is %f" % (x, y, subfun(x, y)))
        else: print("The division of %f and %f is %f" % (x, y, divfun.divfun(x, y)))
op = None
while True:
    op = str(input("Enter the operator + or * or - or / [q = quit]:"))
    if op == '+' or op == '*' or op == '-' or op == '/': break
    if op == 'q': break
if not op == 'q': calc(op)


#!/usr/bin/env python3
def main():
    func(one = 1, two = "two", false = False)
    print()
    new_func(1, "two", False)
    new_func(1, 2, 3, 4)
    new_func(1, 2, 3, five = 5)
    new_func(1, 2, 3, 4, 5, 6, 7, eight = 8, nine = 9, ten = 10)
def func(**kwargs): # They are very commonly called kwargs (kwargs is actually a dictionary)
    print(kwargs['one'], kwargs['two'], kwargs['false'])
    for k, v in kwargs.items():
        print(k, v)
# Note that they must be in that order; that is, our args then *args and then **kwargs
def new_func(this, that, other, *args, **kwargs): # this, that and other args are mandatory while *args and **kwargs are optional
    print(this, that, other, args, type(args), kwargs, type(kwargs))
    print(this, that, other, end = ' ')
    for e in args:
        print(e, end = ' ')
    for k in kwargs:
        print(kwargs[k], end = ' ')
    print()
if __name__ == "__main__": main()

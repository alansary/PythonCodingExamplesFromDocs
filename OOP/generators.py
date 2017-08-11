#!/usr/bin/env python3


def main():
    # obj = Range(100, 0, -2)
    # for e in obj: print(e)
    for x in Range(100, 0, -2): print(x)
    # for i in range(100, -1, -2): print(i)


class Range:
    def __init__(self, *args):
        self.args = args
        if len(self.args) == 1:
            assert type(self.args[0]) is type(0), "TypeError: '{}' object cannot be interpreted as an integer".format(str(type(self.args[0])))
        if len(self.args) == 2:
            assert type(self.args[1]) is type(0), "TypeError: '{}' object cannot be interpreted as an integer".format(str(type(self.args[1])))
        if len(self.args) == 3:
            assert type(self.args[2]) is type(0), "TypeError: '{}' object cannot be interpreted as an integer".format(str(type(self.args[2])))

    # __iter__ makes the object an iterable object (generator)
    # When the object is used in the context of an iterable (for instance, in a for loop), __iter__() method gets called automatically
    # In fact, I don't have to create an object, I can use the name of the class as an iterator
    def __iter__(self):
        if len(self.args) == 0:
            raise TypeError("Range expected 1 arguments, got 0")
        elif len(self.args) > 3:
            raise TypeError("Range expected at most 3 arguments, got 4")
        else:
            if len(self.args) == 1:
                self.start = 0
                self.end = self.args[0]
                self.step = 1
                if self.end <= 1:
                    pass
                else:
                    while self.start < self.end:
                        yield self.start
                        self.start += self.step
            elif len(self.args) == 2:
                self.start = self.args[0]
                self.end = self.args[1]
                self.step = 1
                if self.start >= self.end:
                    pass
                else:
                    while self.start < self.end:
                        yield self.start
                        self.start += self.step
            else:
                self.start = self.args[0]
                self.end = self.args[1]
                self.step = self.args[2]
                if self.step == 0: raise ValueError("Range() arg 3 must not be zero")
                elif self.step > 0:
                    if self.start >= self.end:
                        pass
                    else:
                        while self.start < self.end:
                            yield self.start
                            self.start += self.step
                else:
                    if self.start <= self.end:
                        pass
                    else:
                        while self.start > self.end:
                            yield self.start
                            self.start += self.step


'''
def Range(*args):
    if len(args) == 1:
        assert type(args[0]) is type(0), "TypeError: '{}' object cannot be interpreted as an integer".format(str(type(args[0])))
    if len(args) == 2:
        assert type(args[1]) is type(0), "TypeError: '{}' object cannot be interpreted as an integer".format(str(type(args[1])))
    if len(args) == 3:
        assert type(args[2]) is type(0), "TypeError: '{}' object cannot be interpreted as an integer".format(str(type(args[2])))
    if len(args) == 0:
        raise TypeError("Range expected 1 arguments, got 0")
    elif len(args) > 3:
        raise TypeError("Range expected at most 3 arguments, got 4")
    else:
        if len(args) == 1:
            start = 0
            end = args[0]
            step = 1
            if end <= 1:
                pass
            else:
                while start < end:
                    yield start
                    start += step
        elif len(args) == 2:
            start = args[0]
            end = args[1]
            step = 1
            if start >= end:
                pass
            else:
                while start < end:
                    yield start
                    start += step
        else:
            start = args[0]
            end = args[1]
            step = args[2]
            if step == 0: raise ValueError("Range() arg 3 must not be zero")
            elif step > 0:
                if start >= end:
                    pass
                else:
                    while start < end:
                        yield start
                        start += step
            else:
                if start <= end:
                    pass
                else:
                    while start > end:
                        yield start
                        start += step
'''

if __name__ == "__main__": main()
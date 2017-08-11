#!/usr/bin/python3
def main():
    obj = MyNum()
    print(obj.value)
    obj.increment()
    print(obj.value)

    print('=' * 50)

    obj2 = MyNum2(12.3)
    obj2.increment()
    print(obj2.value)
    obj2.decrement()
    print(obj2.value)
    obj3 = MyNum2('x')
    print(obj3.value)
    obj3.increment()

    print('=' * 50)

    obj4 = MyNum3(12.3)
    obj4.increment()
    print(obj4.value)
    obj4.decrement()
    print(obj4.value)
    obj5 = MyNum3('x')
    obj5.increment()

'''
    Initializing the attributes in the instance at the time of construction
    init == initialization
    This is a private (magic) method, it is intended to be used internally and not called by the user of the class
    It is called magic because it gets called automatically when a particular event happens
    __init__ is called automatically any time a new instance is constructed
'''


class MyNum(object):
    def __init__(self):
        print('Calling __init__')
        self.value = 0

    def increment(self):
        self.value += 1


class MyNum2(object):
    # Enforcing self.value to be declared when instantiating an object (0 or passed value)
    def __init__(self, value):
        try:
            int(value)
        except ValueError as e:
            print(e)
            self.value = 0
            return
        except TypeError as e:
            print(e)
            self.value = 0
            return
        except:
            self.value = 0
            return
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1


class MyNum3(object):
    # self.value will be declared iff int(value) is a valid expression
    def __init__(self, value):
        try:
            int(value)
        except ValueError as e:
            print(e)
            return
        except TypeError as e:
            print(e)
            return
        except:
            return
        self.value = value

    def increment(self):
        # Handling increment - Case the user passed wrong value or type
        try:
            self.value += 1
        except ValueError as e:
            print(e)
            return
        except TypeError as e:
            print(e)
            return
        except:
            print('Error occurred')
            return


    def decrement(self):
        # Handling decrement() - Case the user passed wrong value or type
        try:
            self.value -= 1
        except ValueError as e:
            print(e)
            return
        except TypeError as e:
            print(e)
            return
        except:
            print('Error occurred')
            return

if __name__ == "__main__": main()

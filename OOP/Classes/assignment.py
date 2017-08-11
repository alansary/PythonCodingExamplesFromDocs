#!/usr/bin/python3
def main():
    a = MaxSizeList(3)
    b = MaxSizeList(1)

    a.push('hey')
    print(a.get_list())
    a.push('hi')
    print(a.get_list())
    a.push('let\'s')
    print(a.get_list())
    a.push('go')
    print(a.get_list())

    print('=' * 50)

    b.push('hey')
    print(b.get_list())
    b.push('hi')
    print(b.get_list())
    b.push('let\'s')
    print(b.get_list())
    b.push('go')
    print(b.get_list())

    print('=' * 100)

    x = MaxSizeList2(3)
    y = MaxSizeList2(1)

    x.push('hey')
    x.push('hi')
    x.push('let\'s')
    x.push('go')

    y.push('hey')
    y.push('hi')
    y.push('let\'s')
    y.push('go')

    print(x.get_list())
    print(y.get_list())

'''
    EVALUATING CODE
        - Clarity first!
        - Maintainability (minimal repetition or dependencies)
        - Consistency (syntax, variable naming)
        - Brevity
        - At higher levels, and after the above:
            - Time efficiency
            - Memory efficiency
'''


class MaxSizeList(object):
    # Enforcing data integrity
    # This is not encapsulated instance data, this is a class attribute
    size = 0

    def __init__(self, size):
        # Validate the passed size
        if str(size).isnumeric():
            self.list_size = size
            self.list = list()
        else:
            print('Please, pass a valid length')
            return

    def push(self, element):
        # If the length of the list doesn't exceed the passed size then push the element
        if len(self.list) < self.list_size:
            self.list.append(element)
        else:
            # else, pop the element at index 0, then push the element
            self.list.pop(0)
            self.list.append(element)

    def get_list(self):
        # If the length of the list is the same as the passed size, then return the list as it is
        if not len(self.list) < self.list_size:
            return self.list
        else:
            # else while the length of the list is not the same as the passed size insert None at index 0, and finally
            # return the list
            while len(self.list) != self.list_size:
                self.list.insert(0, None)
            return self.list


class MaxSizeList2(object):
    def __init__(self, max):
        self.size = max
        self.l = list()

    def push(self, element):
        self.l.append(element)
        if len(self.l) > self.size:
            self.l.pop(0)

    def get_list(self):
        return self.l

if __name__ == "__main__": main()
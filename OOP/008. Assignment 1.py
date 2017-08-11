#!/usr/bin/env python3

# Evaluating Code
# Clarity first!
# Maintainability (minimal repetition or dependencies)
# Consistency (syntax, variable naming)
# Brevity
# At higher levels, and after the above:
# Time efficiency
# Memory efficiency

class MaxSizeList(object):
    def __init__(self, maxSize):
        self.l = []
        self.maxSize = maxSize

    def push(self, element):
        self.l.append(element)
        if (len(self.l) > self.maxSize):
            self.l.pop(0)

    def get_list(self):
        return self.l

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())

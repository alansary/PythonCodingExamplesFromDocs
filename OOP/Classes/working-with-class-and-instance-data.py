#!/usr/bin/python3
def main():
    # We are printing the count immediately after the instantiation
    # self.count == InstanceCounter.count == 0
    obj1 = InstanceCounter(10)
    # self.count == InstanceCounter.count == 1
    print(obj1.get_count())
    print(obj1.count)
    print(InstanceCounter.count)
    obj2 = InstanceCounter(20)
    # self.count == InstanceCounter.count == 2
    print(obj2.get_count())
    print(obj2.count)
    print(InstanceCounter.count)
    obj3 = InstanceCounter(30)
    # self.count == InstanceCounter.count == 3
    print(obj3.get_count())
    print(obj3.count)
    print(InstanceCounter.count)

    print('=' * 50)

    # Re-printing the value of the attribute count for all the instance, we will get the most recent value of count
    print(obj1.get_count())
    print(obj1.count)
    print(obj2.get_count())
    print(obj2.count)
    print(obj3.get_count())
    print(obj3.count)
    print(InstanceCounter.count)

    print('=' * 50)

    # The OrderCounter class will associate with each object a new value for the count attribute which is the order
    # of instantiation of this particular class
    # Now each instance preserves its order of instantiation (modified the default value of count for itself) and
    # the count attribute for the class contains the final number of instantiated objects
    obj4 = OrderCounter(40)
    obj5 = OrderCounter(50)
    obj6 = OrderCounter(60)
    print(obj4.get_count())
    print(obj4.count)
    print(OrderCounter.count)
    print(obj5.get_count())
    print(obj5.count)
    print(OrderCounter.count)
    print(obj6.get_count())
    print(obj6.count)
    print(OrderCounter.count)



class InstanceCounter(object):
    # count counts the number of instantiated objects
    count = 0 # This is a global variable within the class, to access it from any function we must precede it with
    # the name of the class

    # Any instantiated object must pass a value as an argument (value attribute of this particular instance)
    # At the time of instantiation we will increment the counter and its value at the mean time which is the
    # number of instantiated objects so far
    def __init__(self, val):
        self.value = val
        InstanceCounter.count += 1 # count is a global variable for this function (obj.attr syntax)

    # We can set a new value for the instance_attribute if we like to
    def set_value(self, newval):
        self.value = newval

    # We can get the value of the instance_attribute value at any time
    def get_value(self):
        return self.value

    # returning the class_attribute count
    def get_count(self):
        return InstanceCounter.count

class OrderCounter(object):
    # count counts the number of the instance in the order of instantiation
    count = 0

    # Any instantiated object must pass a value as an argument (value attribute of this particular instance)
    # We will increment the count and update the value of the class attribute count for this particular instance
    # to save its order of instantiation
    def __init__(self, val):
        self.value = val
        OrderCounter.count += 1
        self.count = OrderCounter.count

    # We can set a new value for the instance_attribute if we like to
    def set_value(self, newval):
        self.value = newval

    # We can get the value of the instance_attribute value at any time
    def get_value(self):
        return self.value

    # returning the class_attribute count that is associated with this particular instance
    def get_count(self):
        return self.count

if __name__ == "__main__": main()
test_list = [1, 2, 3]
print("The list is %r" % test_list)
print("Inserting elements")
# Checking the number of the elements to insert
num = None
while type(num) != type(0) or num <= 0:
    try:
        num = int(input("Enter the number of elements to insert:"))
    except:
        print("The number of the elements must be an integer greater than 0")
counter = 0
while counter != num:
    counter += 1
    print("Inserting the element number %d" % counter)
    # Checking the index of the element
    index = -1
    while not 0 <= index <= len(test_list):
        try:
            print("The index of the element must be from 0 to %d" % len(test_list))
            index = int(input("Enter the index of the element:"))
        except:
            print("The index of the element must be an integer")
    value = None
    # Checking the value of the element
    while type(value) != type(0):
        try:
            value = int(input("Enter the value of the element:"))
        except:
            print("The value of the element must be an integer")
    print("Inserting the value %d into the index %d" % (value, index))
    test_list.insert(index, value)
    print("The list now is %r" % test_list)
try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print(e)
try:
    print(1)
    assert 2 + 2 == 5
except AssertionError:
    print(3)
except:
    print(4)  # Will not print
# During handling of the above exception, another exception occurred:
    # Caused by raising an exception while another exception is already raised
    #except:
        # raise SyntaxError/RuntimeError/ZeroDivisionError/IndexError/ValueError/Exception/IOError/FileNotFoundError/
        # NameError("Message")

# The above exception was the direct cause of the following exception:
    # except Exception as abbreviation:
        # raise SyntaxError/RuntimeError/ZeroDivisionError/IndexError/ValueError/Exception/IOError/FileNotFoundError/
        # NameError("Message") from abbreviation

# raise Exception("This is an exception")
# raise ValueError("This is a value error")
# raise IndexError("This is an index error")
# raise ZeroDivisionError("This is a zero division error")
# raise RuntimeError("This is a runtime error")
# raise SyntaxError("This is a syntax error")
# raise NameError("This is a name error")

# The above exception was the direct cause of the following exception: RuntimeError: You can not divide by zero (Undefined)
'''
x = int(input("Enter a value:"))
try:
    print(x/0)
except Exception as exp:
    raise RuntimeError("You can not divide by zero (Undefined)") from exp
'''
# During handling of the above exception, another exception occurred: RuntimeError: You can not divied by zero (Undefined)
'''
x = int(input("Enter a value:"))
try:
    print(x/0) # will raise a ZeroDivisionError
except:
    raise RuntimeError("You can not divide by zero (Undefined)")
'''
# During handling of the above exception, another exception occurred: ZeroDivisionError: You can not divide by zero (Undefined)
'''
x = int(input("Enter a value:"))
try:
    print(x/0)
except:
    raise ZeroDivisionError("You can not divide by zero (Undefined)")
'''
# The above exception was the direct cause of the following exception: IndexError: The index must be an integer
'''
test_list = [1, 2, 3]
print("The list is %r" % test_list)
while True:
    index = input("Enter the index [q = quit]:")
    if index == 'q': break
    try:
        index = int(index)
        if not 0 <= index < len(test_list):
            print("The index must be greater than or equal to 0 and less than %d" % len(test_list))
        else:
            break
    except Exception as exp:
        raise IndexError("The index must be an integer") from exp
'''
'''
# During handling of the above exception, another exception occurred: IndexError: The index must be an integer
test_list = [1, 2, 3]
print("The list is %r" % test_list)
while True:
    index = input("Enter the index [q = quit]:")
    if index == 'q': break
    try:
        index = int(index)
        if not 0 <= index < len(test_list):
            print("The index must be greater than or equal to 0 and less than %d" % len(test_list))
        else:
            break
    except:
        raise IndexError("The index must be an integer")
# The above exception was the direct cause of the following exception: ValueError: I want an integral value
while True:
    value = input("Enter the value [q = quit]:")
    if value == 'q': break
    try:
        value = int(value)
        break
    except Exception as exp:
        raise ValueError("I want an integral value") from exp
'''

# Handling the error within the function
def readfile(fileName):
    try:
        fileHandle = open(fileName, 'r')
        return fileHandle.readlines() # Iterator
    except IOError as err:
        print(err)
        return () # Empty Iterator
for line in readfile('test-file.txt'):
    print(line.strip())
for line in readfile('not-exist.txt'):
    print(line.strip())

print('\n' * 2)

# Handling the error in the function call
def readfile2(fileName):
    fh = open(fileName, 'r')
    return fh.readlines() # Iterator
for line in readfile2('test-file.txt'):
    print(line.strip())
try:
    for line in readfile2('not-exist.txt'):
        print(line.strip())
except IOError as e:
    print(e)

print('\n' * 2)

# Raising our own exceptions
def readfile3(fileName):
    if fileName.endswith('.txt'):
        fh = open(fileName, 'r')
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
try:
    for line in readfile3('test-file.txt'):
        print(line.strip())
except IOError as e:
    print('Cannot read file:', e)
except ValueError as e:
    print('Bad filename:', e)
try:
    for line in readfile3('not-exist.txt'):
        print(line.strip())
except IOError as e:
    print('Cannot read file:', e)
except ValueError as e:
    print('Bad filename:', e)
try:
    for line in readfile3('test-file.doc'):
        print(line.strip())
except IOError as e:
    print('Cannot read file:', e)
except ValueError as e:
    print('Bad filename:', e)

print('\n' * 2)

test_list = [1, 2, 3]
print("The list is %r" % test_list)
while True:
    index = input("Enter the index [q = quit]:")
    if index == 'q': break
    try:
        index = int(index)
        print(test_list[index])
    except IndexError as err: # Error with the index (it is integer but there is something went wrong when accessing the value)
        print(err)
    except Exception as exp: # It is not an integer
        print(exp)


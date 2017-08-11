#!/usr/bin/env python3
def main():
    # FileNotFoundError is the name of the exception raised by the python interpreter when the file doesn't exist
    # IOError is the name of the exception raised by the python interpreter when it fails to open a file for some reason

    # fh = open('does-not-exist.txt', 'r') will raise a FileNotLFoundError
    try:
        fh = open('test-file.txt', 'r')
    except IOError as e:
        print(e)
    else: # else gets executed if except doesn't execute that means if try succeeded, then else will execute
        for line in fh:
            print(line, end = '')
    print('\n' * 2)
    try:
        fh = open('not-exist.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    else: # else will not execute since except will be executed
        for line in fh:
            print(line, end = '')
    print('\n' * 2)
    fh = open('test-file.txt', 'r')
    try:
        fh.write('This is the fourth line')
    except IOError as e:
        print(e)
    # Will raise an io.UnsupportedOperation since the file is opened in read mode we can not use write() method
    print('\n' * 2)
    try:
        # fh = open('test-file.txt', 'r')
        fh = open('not-exist.txt', 'r')
        print("Succedded")
    except IOError as err:  # It is better with files to always use IOError rather than FileNotFoundError
                            # (FileNotFoundError is in IOError)
        print(err)
    # except FileNotFoundError as e:
    #     print(e)
if __name__=="__main__": main()
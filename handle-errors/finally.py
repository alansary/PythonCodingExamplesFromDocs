#!/usr/bin/env python3

# To ensure some code runs no matter what errors occur, you can use a finally statement.
# The finally statement is placed at the bottom of a try/except statement. Code within a finally statment always
# runs after execution of the code in the try, and possibly in the except, blocks.10
# Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks.

def main():
    x = input("Enter the first number:")
    y = input("Enter the second number:")
    try:
        x = float(x)
        y = float(y)
        print(x / y)
    except ZeroDivisionError as e:
        print(e)
    except (TypeError, ValueError) as e:
        print(e)
    finally:
        print("This print statement will run no matter what")

    # try:
    #     print(1/0)
    # except ZeroDivisionError:
    #     raise ValueError

    # using raise without specifying the error will re-raise whatever exception occurred
    try:
        print(1/0)
    except:
        raise

    try:
        print(1)
        print(10/0)
    except ZeroDivisionError:
        print(unknown_var)
    finally:
        print("This is executed last")

if __name__ == "__main__": main()

# Function Definition
def print_fun():
    print("We are in")
# Function Call
print_fun()
def call_fun(fun):
    fun()
call_fun(print_fun)
def add_fun(arg1, arg2):
    print(arg1 + arg2)
add_fun(2, 3)
def call_fun2(fun, arg1, arg2):
    fun(arg1, arg2)
call_fun2(add_fun, 2, 3)
def true_fun():
    return True
if true_fun(): print("True")
else: print("False")
def test_fun(ahmed):
    return ahmed + ' ' + ahmed
print(test_fun("Mohamed"))
def color_fun(color):
    if color == "Yellow":
        return "This is banana"
    elif color == "Red":
        return "This is tomato"
    elif color == "Ali":
        print("This is not a color")
    else:
        print("I don't know")
print(color_fun("Yellow"))
print(color_fun("Red"))
color_fun("Ali")
color_fun("Any thing else")


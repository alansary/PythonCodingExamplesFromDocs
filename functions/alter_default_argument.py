# Important: Creating a default mutable argument, calling the function many times and altering the value of this argument, we will find that any
#	     modifications we make to this argument will be reserved for this default argument. That is, it is reserved in the memory.
# However any other passed argument is garbage collected once the function call returns.
print("Case I: Defining a function with a default argument that we modify each time we call the function.")
def my_fun(arg, result = []):
    result.append(arg)
    print(result)
my_fun('a')
my_fun('b')
my_fun('c')
my_fun('z', ['x', 'y'])
my_fun('a')
my_fun('a', ['x', 'y'])
my_fun('b', [])
print("Case II: Defining a function that contains a variable that we modify each time we call the function.")
def my_fun(arg):
    result = []
    result.append(arg)
    print(result)
my_fun('a')
my_fun('b')
my_fun('c')
my_fun('z')
my_fun('a')
my_fun('a')
my_fun('b')
print("Case III: Defining a function with two positional arguments")
def my_fun(arg, result):
    result.append(arg)
    print(result)
my_fun('a', [])
my_fun('b', [])
my_fun('c', [])
my_fun('z', ['x', 'y'])
my_fun('a', [])
my_fun('a', ['x', 'y'])
my_fun('b', [])
print("Case IV: Defining a function with a default argument that is initialized to None")
def my_fun(arg, result = None):
    if result == None:
        result = []
    result.append(arg)
    print(result)
my_fun('a')
my_fun('b')
my_fun('c')
my_fun('z', ['x', 'y'])
my_fun('a')
my_fun('a', ['x', 'y'])
my_fun('b', [])


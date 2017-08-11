def test_fun(coca, tea, coffee):
    return {"Coca":coca, "Tea":tea, "Coffee":coffee}
print(test_fun(3, 5, 2))
print(test_fun(coca = 3, tea = 5, coffee = 2))
# Create an argument that has a default value
	# non-default arguments must not follow a default argument
def fun(arg = True):
    if arg: print("True")
    else: print("False")
fun()
fun(True)
fun(False)
# In the following function, arg1 and arg2 are positional arguments and arg3 and arg4 are default arguments
def fun2(arg1, arg2, arg3 = 2, arg4 = 3):
    print("The numbers are %d, %d, %d, and %d, their sum is:" % (arg1, arg2, arg3, arg4))
    print(arg1 + arg2 + arg3 + arg4)
fun2(5, 1)
fun2(5, 1, 6)
fun2(5, 1, 6, 7)


# Operator Precedence is PEMDAS (Parentheses, Exponentiation, Multiplication, Division, Addition, Subtraction)
    # P
    # E
    # M D (Associativity: left to right)
    # A S (Associativity: left to right)
x, y = 7, 2
print("{} divided by {} is {} (true division)".format(x, y, x / y))
print("{} divided by {} is {} (floor/integer/truncated division)".format(x, y, x // y))
print("{} is the remainder of division of {} over {} (modulo)".format(x % y, x, y))
print("{} are the values of the quotient and the remainder of division of {} over {}".format(divmod(x, y), x, y))
print("Rounding the result of division of {} over {} to the nearest integer, we get {}".format(x, y, round(x / y)))
print("Rounding the result of division of {} over {} to the nearest tenth, we get {}".format(x, y, round(x / y, 1)))
print("Rounding the result of division of {} over {} to the nearest hundredth, we get {}".format(x, y, round(x / y, 2)))
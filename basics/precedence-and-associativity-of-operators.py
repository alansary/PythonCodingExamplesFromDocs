#!/usr/bin/env python3
def main():
    pass
'''
# https://docs.python.org/3/reference/expressions.html
    Associativity                                       operators                                       Description
    left to right                                        lambda                                     Lambda Expression
    left to right                                           or                                          Boolean
    left to right                                          and                                          Boolean
    left to right                                          not                                          Boolean
    right to left                       in, not in, is, is not, <, <=, >, >=, !=, ==                   Comparisons
    left to right                                           |                                           Bitwise
    left to right                                           ^                                           Bitwise
    left to right                                           &                                           Bitwise
    left to right                                         <<, >>                                    Bitwise shift
    left to right                                          +, -                                        Arithmetic
    left to right                                      *, /, //, %                                     Arithmetic
        N/A                                            +x, -x, ~x                                   Unary Arithmetic
    left to right                                           **                                       Exponentiation
    right to left                       x[slice], x(arguments...), x.attribute          Slice, function call and attribute reference
    left to right                       (expression...), [expression...], {key:value}       Binding, tuple, list and dictionary
    # binding: The parentheses when not meant to be a tuple.

    Precedence and Associativity of Operators in Python
        Expression
            The combination of values, variables, operators and function calls is termed as an expression.
        Precedence
            To evaluate these type of expressions there is a rule of precedence in Python. It guides the order in which operation are
            carried out. But we can change this order using parentheses () as it has higher precedence.
            he precedence of operators in Python are listed in the following table. It is in descending order, upper group has higher
            precedence than the lower ones.
                Operator precedence rule in Python
                    Operators                           	                Meaning
                    ()	                                                    Parentheses
                    **	                                                    Exponent
                    +x, -x, ~x	                                            Unary plus, Unary minus, Bitwise NOT
                    *, /, //, %	                                            Multiplication, Division, Floor division, Modulus
                    +, -	                                                Addition, Subtraction
                    <<, >>	                                                Bitwise shift operators
                    &	                                                    Bitwise AND
                    ^	                                                    Bitwise XOR
                    |	                                                    Bitwise OR
                    ==, !=, >, >=, <, <=, is, is not, in, not in	        Comparisions, Identity, Membership operators
                    not	                                                    Logical NOT
                    and	                                                    Logical AND
                    or	                                                    Logical OR
        Associativity
            We can see in the above table that more than one operator exist in the same group. These operators have the same
            precedence. Associativity is the order in which an expression is evaluated that has multiple operator of the same
            precedence.
        Non associative operators
            Some operators like assignment operators and comparison operators do not have associativity in Python. There are separate
            rules for sequences of this kind of operator and cannot be expressed as associativity. For example, x < y < z neither
            means (x < y) < z nor x < (y < z). x < y < z is equivalent to x < y and y < z, and is evaluates from left-to-right.
            Furthermore, while chaining of assignments like x = y = z is perfectly valid, x = y += z will result in error.
'''
if __name__ == "__main__": main()

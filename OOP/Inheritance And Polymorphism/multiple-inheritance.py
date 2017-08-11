#!/usr/bin/python3
def main():
    # This is the first case where A is the grandparent of D and parent of B, B and C are parents of D
    d_obj = D()
    # We implemented the same interface of the search_method() method within the class A which is the grandparent
    # of the class D and also within the class C which is the parent of the class D
    # Python will first lookup the attribute search_method() within the first passed parent class which is C
    # then if it doesn't exist within the parent class C, it will check to see it the parent class C also has
    # a parent, if it does, then it will check the class A which is the parent of the class C and the grandparent
    # of the class D to see if the attribute exists, if it does it will call it from the class A
    # And so on till it finds it in this tree (hierarchy), then it will go to the other parent to search it following
    # the same way.
    # In our case -> following the depth-first search -> D -> B -> A -> C
    d_obj.search_method()
    print(D.mro()) # This is the method resolution order built-in function that shows us the path Python takes in
    # searching for an attribute of some class

    # This is the second case where A2 is the parent of both B2 and C2 and a grandparent of D2, B2 and C2 are both
    # parents to D2
    # "Diamond shape" inheritance has ambiguous order
    # To remove the ambiguity of D2 -> B2 -> A2 -> C2 -> A2 of depth-first search in this case (where A2 is repeated)
    # The way Python handle the ambiguity is to remove earlier appearances of multiply refereed to classes (A2)
    # It removes the earlier occurrence of A2
    # D2 -> B2 -> A2 -> C2 -> A2 will be D2 -> B2 -> C3 -> A2 (The early occurrence of A2 has been removed)
    # It looks like a breadth-first search but it is not (it is just removing the first occurrence of A2)
    # It just appends the following rule to the depth-first search:
    # If the same class appears in a method resolution order, the earlier occurrences of this class are removed from
    # the method resolution order
    d2_obj = D2()
    d2_obj.search_method()
    print(D2.mro())

'''
    MULTIPLE INHERITANCE (depth-first or breadth-first ?)
        - Python uses the depth-first search for an attribute (When searching inheriting classes)
        - Appends the rule "If the same class appears in a method resolution order, the earlier occurrences of this
          class are removed from the method resolution order"
        - You can use the method resolution order mro() to see what is the order it follows
        - The above applies to "new style" classes (inheriting from object)
'''


# This is the parent class of the class B and the grandparent class of the class D
class A(object):

    def search_method(self):
        print('This is search method from the class A')

    def a_method(self):
        print('I\'m the method within the class A')


# This is the child class of the class A and the parent class of the class D
class B(A):

    def b_method(self):
        print('I\'m the method within the class B')


# This is the parent class of the class D
class C(object):

    def search_method(self):
        print('This is search method from the class C')

    def c_method(self):
        print('I\'m the method within the class C')


# This is the child class of the class B and also the child class of the class C
class D(B, C):

    def d_method(self):
        print('I\'m the method within the class D')


class A2(object):

    def search_method(self):
        print("This is the search method within the class A2")

    def a2_method(self):
        print("I'm the method within the class A2")


class B2(A2):

    def b2_method(self):
        print("I'm the method within the class B2")


class C2(A2):

    def search_method(self):
        print("This is the search method within the class C2")

    def c2_method(self):
        print("I'm the method within the class C2")


class D2(B2, C2):

    def d2_method(self):
        print("I'm the method within the class D2")

if __name__ == "__main__": main()
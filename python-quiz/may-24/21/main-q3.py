"""
What will be the output?
a) A method
b) B method
c) Error
d) Both A and B methods
"""

class A:
    def method(self):
        print("A method")

class B:
    def method(self):
        print("B method")

class C(A, B):
    pass

c = C()
c.method()

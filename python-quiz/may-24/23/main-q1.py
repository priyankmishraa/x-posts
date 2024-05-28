"""
What will be the output?
a) B process
b) C process
c) A process
d) Error

"""

class A:
    def process(self):
        print("A process")

class B(A):
    def process(self):
        print("B process")

class C(A):
    def process(self):
        print("C process")

class D(B, C):
    pass

d = D()
d.process()

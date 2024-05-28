"""
What will be the output?
a) A's init called
b) B's init called
c) A's init called
B's init called
d) Error
"""
class A:
    def __init__(self):
        print("A's init called")

class B(A):
    def __init__(self):
        super().__init__()
        print("B's init called")

b = B()

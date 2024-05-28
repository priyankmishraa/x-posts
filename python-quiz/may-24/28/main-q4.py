"""
What will be the output?
a) True
b) False
c) None
d) Error
"""

class A:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

a = A(10)
b = A(20)
print(a < b)

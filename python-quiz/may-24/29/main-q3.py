"""
What will be the output?
a) Error
b) None
c) Alice 30 Wonderland
d) Alice 30
"""

class MyClass:
    __slots__ = ['name', 'age']

obj = MyClass()
obj.name = "Alice"
obj.age = 30
obj.address = "Wonderland"
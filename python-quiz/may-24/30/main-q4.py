"""
What will be the output?
a) str method
repr method
b) repr method
str method
c) Error
d) None
"""

class MyClass:
    def __str__(self):
        return "str method"

    def __repr__(self):
        return "repr method"

obj = MyClass()
print(str(obj))
print(repr(obj))

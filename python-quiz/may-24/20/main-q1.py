"""
What will be the output?
a) class method called
b) Error
c) None
d) self is not defined
"""

class MyClass:
    @classmethod
    def class_method(cls):
        return "class method called"

print(MyClass.class_method())

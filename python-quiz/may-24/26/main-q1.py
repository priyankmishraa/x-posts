"""
What will be the output?
a) class variable
class variable
b) Error
c) None
d) self is not defined
"""

class Test:
    class_var = "class variable"

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    def static_method():
        return Test.class_var

print(Test.class_method())
print(Test.static_method())

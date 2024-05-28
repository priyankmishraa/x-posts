"""
What will be the output?
a) static method called
b) Error
c) None
d) self is not defined

"""

class MyClass:
    @staticmethod
    def static_method():
        return "static method called"

print(MyClass.static_method())

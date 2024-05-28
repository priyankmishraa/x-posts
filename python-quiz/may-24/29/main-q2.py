"""
What will be the output?
a) Getting value
b) Setting value
Getting value
c) Error
d) None

"""

class Descriptor:
    def __get__(self, instance, owner):
        return "Getting value"

    def __set__(self, instance, value):
        print("Setting value")

class MyClass:
    attr = Descriptor()

obj = MyClass()
obj.attr = 10
print(obj.attr)

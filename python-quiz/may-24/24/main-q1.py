"""
What will be the output?
a) 10
b) None
c) Error
d) 0
"""
class MyClass:
    def __init__(self, value):
        self.__value = value

    def __private_method(self):
        return self.__value

    def public_method(self):
        return self.__private_method()

obj = MyClass(10)
print(obj.public_method())

"""
What will be the output?
a) MetaClass
b) Error
c) None
d) MyClass
"""

class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['category'] = 'MetaClass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.category)


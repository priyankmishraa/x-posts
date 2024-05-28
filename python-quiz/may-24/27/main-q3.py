"""
What will be the output?
a) 0
b) 1
c) 2
d) Error
"""

class MyClass:
    counter = 0

    def __init__(self):
        MyClass.counter += 1

a = MyClass()
b = MyClass()
print(MyClass.counter)
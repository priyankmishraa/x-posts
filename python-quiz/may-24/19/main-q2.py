"""
What will be the output?
a) Hello from Parent
b) Hello from Child
c) None
d) Error
"""

class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

child = Child()
print(child.greet())

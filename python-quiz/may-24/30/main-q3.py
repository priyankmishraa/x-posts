"""
What will be the output?
a) class variable instance variable
b) Error
c) instance variable class variable
d) None
"""

class MyClass:
    class_var = "class variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var

a = MyClass("instance variable")
print(a.class_var, a.instance_var)

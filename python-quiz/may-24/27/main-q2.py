"""
What will be the output?
a) Hello
b) Error
c) None
d) new_attr
"""

class Dynamic:
    pass

obj = Dynamic()
obj.new_attr = "Hello"
print(obj.new_attr)
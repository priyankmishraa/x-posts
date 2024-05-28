"""
What will be the output?
a) True
b) False
c) None
d) Error
"""

class Box:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

box1 = Box(10)
box2 = Box(10)
print(box1 == box2)

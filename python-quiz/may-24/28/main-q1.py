"""
What will be the output?
a) 20
b) 9
c) Error
d) None
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print(rect.area)
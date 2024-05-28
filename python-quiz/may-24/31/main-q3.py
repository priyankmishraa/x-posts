"""
What will be the output?
a) RED 1
b) 1 RED
c) Error
d) None
"""

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name, Color.RED.value)
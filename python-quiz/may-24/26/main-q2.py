"""
What will be the output?
a) True
b) False
c) None
d) Error
"""

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
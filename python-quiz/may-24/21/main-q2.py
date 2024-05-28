"""
What will be the output?
a) Base init
b) Derived init
c) None
d) Error
"""

class Base:
    def __init__(self):
        print("Base init")

class Derived(Base):
    pass

d = Derived()

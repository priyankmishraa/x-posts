"""
What will be the output?
a) 10
b) Error
c) None
d) inner
"""

class Outer:
    class Inner:
        def __init__(self, value):
            self.value = value

    def __init__(self, value):
        self.inner = self.Inner(value)

outer = Outer(10)
print(outer.inner.value)
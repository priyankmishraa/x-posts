"""
What will be the output?
a) 10
b) 5
c) 15
d) 0
"""

class Math:
    def __init__(self, value=0):
        self.value = value

    def add(self, amount):
        self.value += amount
        return self

    def subtract(self, amount):
        self.value -= amount
        return self

result = Math().add(10).subtract(5).value
print(result)
"""
What will be the output?
a) Hello, my name is Alice and I am 30 years old.
b) Error
c) None
d) Alice 30

"""

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p = Person("Alice", 30)
print(p.greet())

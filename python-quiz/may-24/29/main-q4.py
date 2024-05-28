"""
What will be the output?
a) Woof! Sleeping
b) Error
c) None
d) Sleeping Woof!
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        return "Sleeping"

class Dog(Animal):
    def sound(self):
        return "Woof!"

dog = Dog()
print(dog.sound(), dog.sleep())

"""
What will be the output?
a) Woof!
b) Buddy
c) None
d) Error
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())

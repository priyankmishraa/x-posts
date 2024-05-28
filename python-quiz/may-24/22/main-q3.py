"""
What will be the output?
a) Engine started
Car started
b) Car started
c) None
d) Error

"""

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")

car = Car()
car.start()

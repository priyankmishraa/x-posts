"""
What will be the output?
a) HELLO
b) hello
c) Error
d) None
"""

def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

class Greet:
    @uppercase_decorator
    def say_hello(self):
        return "hello"

g = Greet()
print(g.say_hello())

"""
What will be the output?
a) Entering context
Inside context
Exiting context
b) Inside context
Entering context
Exiting context
c) Error
d) None
"""

class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext():
    print("Inside context")

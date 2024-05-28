"""
What will be the output?
a) 1 2
1
No arguments
b) 1 2
No arguments
No arguments
c) Error
d) None
"""

class Sample:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(a, b)
        elif a is not None:
            print(a)
        else:
            print("No arguments")

s = Sample()
s.display(1, 2)
s.display(1)
s.display()
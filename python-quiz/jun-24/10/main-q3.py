"""
What will be the output?

1. 3 2 1
2. 2 1 0
3. 3 2 1 0
4. 2 1

"""

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        else:
            self.start -= 1
            return self.start + 1

for num in Countdown(3):
    print(num)

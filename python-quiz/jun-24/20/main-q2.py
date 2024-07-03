"""
What will be the output?

1. 0 2 4 6 8
2. 0 2 4 6 8 10
3. 2 4 6 8 10
4. 0 1 2 3 4

"""

class StepRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += self.step
        return self.current - self.step

for number in StepRange(0, 10, 2):
    print(number)

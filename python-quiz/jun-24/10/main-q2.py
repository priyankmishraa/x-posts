"""
What will be the output?

1. 1 2 3
2. 1 2 3 4
3. 0 1 2 3
4. 2 3 4

"""

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in MyRange(1, 4):
    print(num)

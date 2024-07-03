"""
What will be the output?

1. 3 4
2. 3 4 5
3. 3 4 5 6
4. 3 5

"""
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for c in Counter(3, 5):
    print(c)

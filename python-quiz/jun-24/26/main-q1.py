"""
What will be the output?

1. 5 4 3 2 1
2. 4 3 2 1 0
3. 5 4 3 2 1 0
4. 4 3 2 1

"""
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for num in CountDown(5):
    print(num)

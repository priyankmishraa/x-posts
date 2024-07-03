"""
What will be the output?

1. 0 1 2 3 4
2. 0 1 4 9 16
3. 1 4 9 16 25
4. 0 1 4 9

"""
class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i ** 2
        self.i += 1
        return result

for square in Squares(5):
    print(square)

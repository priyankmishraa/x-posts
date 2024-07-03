"""
What will be the output?

1. H e l l o
2. o l l e H
3. o l l e
4. H e l o

"""

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for char in Reverse('Hello'):
    print(char)

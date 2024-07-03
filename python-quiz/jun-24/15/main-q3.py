"""
What will be the output?

1. 1 2 3
2. 1 2
3. 2 3
3. 3 2 1

"""

data = [1, 2, 3]
iterator = iter(data)
for i in range(2):
    print(next(iterator))

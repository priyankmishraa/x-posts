"""
What will be the output?

1. 1 2 3
2. 2 3 4
3. 1 2 3 4
4. 3 2 1

"""

data = [1, 2, 3, 4]
iterator = iter(data)
for i in range(len(data)):
    print(next(iterator))

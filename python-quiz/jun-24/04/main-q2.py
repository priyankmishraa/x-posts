"""
What will be the output?

1. 0 x, 1 y, 2 z
2. 1 x, 2 y, 3 z
3. x 1, y 2, z 3
4. x y z 1 2 3

"""

data = ['x', 'y', 'z']
for index, value in enumerate(data, start=1):
    print(index, value)

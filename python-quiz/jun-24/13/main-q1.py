"""
What will be the output?

1. x 10 y 20 z 30
2. y 20 z 30
3. x 10
4. z 30

"""

data = {'x': 10, 'y': 20, 'z': 30}
for key in data:
    if data[key] > 15:
        print(key, data[key])

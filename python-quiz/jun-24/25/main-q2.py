"""
What will be the output?

1. {'x': 9, 'y': 8, 'z': 7}
2. {'y': 8, 'z': 7}
3. {'x': 9, 'z': 7}
4. {'x': 8, 'y': 7}

"""
keys = ['x', 'y', 'z']
values = [9, 8, 7]
dictionary = {k: v for k, v in zip(keys, values) if v < 9}
print(dictionary)

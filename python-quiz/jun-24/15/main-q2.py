"""
What will be the output?

1. {'a': 1, 'b': 2, 'c': 3}
2. {'b': 2, 'c': 3}
3. {'a': 2, 'b': 3}
4. {'b': 1, 'c': 2}

"""

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values) if v > 1}
print(dictionary)

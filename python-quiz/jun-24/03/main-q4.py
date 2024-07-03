"""
What will be the output?

1. a 1 b 2 c 3
2. a: 1, b: 2, c: 3
3. 1 a, 2 b, 3 c
4. a-1, b-2, c-3
"""

data = {'a': 1, 'b': 2, 'c': 3}
for key, value in data.items():
    print(key, value)

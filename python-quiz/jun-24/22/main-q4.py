"""
What will be the output?

1. a 1 b 2
2. a 1
3. b 2 c 3
4. a 1 b 2 c 3

"""
data = {'a': 1, 'b': 2, 'c': 3}
for key, value in data.items():
    if value > 2:
        break
    print(key, value)

"""
What will be the output?

1. [(0, 1), (1, 2)]
2. [(0, 0), (1, 1), (2, 2)]
3. [(0, 0), (0, 1), (1, 0), (1, 1)]
4. [(0, 1), (1, 0), (1, 1)]

"""
data = [(x, y) for x in range(2) for y in range(2)]
print(data)

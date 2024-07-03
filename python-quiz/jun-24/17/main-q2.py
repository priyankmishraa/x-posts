"""
What will be the output?

1. [[[0, 0, 0], [0, 1, 0], [0, 2, 0]], [[1, 0, 0], [1, 1, 0], [1, 2, 0]]]
2. [[[0, 0], [0, 1]], [[1, 0], [1, 1]]]
3. [[[0, 0, 0], [0, 0, 1]], [[1, 0, 0], [1, 0, 1]]]
4. [[[0, 0, 0], [0, 1, 0]], [[1, 0, 0], [1, 1, 0]]]

"""

matrix = [[[[i, j, k] for k in range(2)] for j in range(2)] for i in range(2)]
print(matrix)
"""
What will be the output?

1. [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
2. [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
3. [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
4. [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
"""
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

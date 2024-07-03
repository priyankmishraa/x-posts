"""
What will be the output?

1. [[0, 0, 0], [1, 2, 3], [2, 3, 4]]
2. [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
3. [[0, 0, 0], [1, 2, 3], [2, 4, 6]]
4. [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

"""
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)

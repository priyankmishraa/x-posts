"""
What will be the output?

1. 1 2 3 4 5 6 7 8 9
2. 1 3 5 7 9
3. 2 4 6 8
4. 1 3 4 5 7 9

"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for val in row:
        if val % 2 == 0:
            continue
        print(val)

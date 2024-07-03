"""
What will be the output?

1. 1 2 3 4
2. 1 2 3 4 5
3. 1 2 3 4 5 6 7 8 9
4. 1 2 3

"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        if num == 5:
            break
        print(num)
    else:
        continue
    break

"""
What will be the output?

1. i: 0, j: 0 i: 0, j: 1 i: 0, j: 2 i: 1, j: 0 i: 1, j: 1 i: 1, j: 2 i: 2, j: 0 i: 2, j: 1
2. i: 0, j: 0 i: 0, j: 1 i: 0, j: 2 i: 1, j: 0 i: 1, j: 1 i: 1, j: 2 i: 2, j: 0
3. i: 0, j: 0 i: 0, j: 1 i: 1, j: 0 i: 1, j: 1 i: 2, j: 0 i: 2, j: 1
4. i: 0, j: 0 i: 1, j: 0 i: 2, j: 0 i: 2, j: 1

"""
for i in range(3):
    for j in range(3):
        if i + j == 4:
            break
        print(f"i: {i}, j: {j}")

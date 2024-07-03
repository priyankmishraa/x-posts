"""
What will be the output?

1. i: 0, j: 0 i: 1, j: 1 i: 2, j: 2
2. i: 0, j: 0 i: 1, j: 0 i: 1, j: 1
3. i: 1, j: 0 i: 2, j: 0 i: 2, j: 1
4. i: 1, j: 0 i: 2, j: 0 i: 2, j: 1

"""

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(f"i: {i}, j: {j}")

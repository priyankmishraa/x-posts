"""
What will be the output?

1. 0 0 1 0
2. 0 0 0 1 1 0 1 1
3. 0 0 1 0 1 1
4. 0 1 1 1

"""
for i in range(2):
    for j in range(2):
        if j == 1:
            break
        print(i, j)

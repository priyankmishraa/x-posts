"""
What will be the output?

1. 0 1 2 3
2. 0 1 3
3. 0 1 3 4
4. 0 1 2 3 4

"""

for i in range(5):
    if i == 2:
        pass
    elif i == 4:
        break
    print(i)

"""
What will be the output?

1. 1 3 5
2. 1 3
3. 1 3 4
4. 0 1 3 5

"""

for i in range(7):
    if i % 2 == 0:
        continue
    if i == 5:
        break
    print(i)

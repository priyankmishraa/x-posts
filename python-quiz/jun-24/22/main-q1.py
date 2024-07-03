"""
What will be the output?

1. 1 3 5
2. 1 3
3. 1 3 4
4. 1 3 4 5

"""
for i in range(6):
    if i % 2 == 0:
        continue
    if i == 5:
        break
    print(i)

"""
What will be the output?

1. [2, 4, 6, 8, 10]
2. [4, 8]
3. [2, 4, 8, 10]
4. [6, 8]

"""
data = [2, 4, 6, 8, 10]
filtered = [x for x in data if x % 4 == 0]
print(filtered)

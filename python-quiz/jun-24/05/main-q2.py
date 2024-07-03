"""
What will be the output?

1. [1, 2, 3, 4, 5]
2. [2, 4]
3. [1, 3, 5]
4. [0, 2, 4]

"""

data = [1, 2, 3, 4, 5]
filtered_data = [x for x in data if x % 2 == 0]
print(filtered_data)

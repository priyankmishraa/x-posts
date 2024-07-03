"""
What will be the output?

1. [1, 9, 25]
2. [1, 4, 9, 16, 25]
3. [1, 4, 9, 25]
4. [1, 9]

"""

data = [1, 2, 3, 4, 5]
squared = [x**2 for x in data if x % 2 == 1]
print(squared)

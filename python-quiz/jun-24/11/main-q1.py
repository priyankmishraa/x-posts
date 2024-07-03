"""
What will be the output?

1. 2 No break encountered
2. 2 4 No break encountered
3. 2 4 6
4. 2 4

"""

data = [2, 4, 6, 8, 10]
for num in data:
    if num % 4 == 0:
        break
    print(num)
else:
    print("No break encountered")

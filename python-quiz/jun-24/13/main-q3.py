"""
What will be the output?

1. 1: apple 2: banana 3: cherry
2. 2: banana
3. 1: apple 3: cherry
4. 2: cherry

"""

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    if index % 2 == 0:
        print(f"{index}: {fruit}")

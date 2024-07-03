"""
What will be the output?

1. 0 1 2 3 4
2. 0 2 4
3. 2 4
4. 1 3 5

"""

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(5):
    print(num)

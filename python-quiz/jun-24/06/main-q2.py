"""
What will be the output?

1. 3 2 1
2. 1 2 3
3. 3 2 1 0
4. 0 1 2 3

"""

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)

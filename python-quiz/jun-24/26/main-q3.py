"""
What will be the output?

1. 4 3 2 1
2. 3 2 1
3. 4 3 2 1 0
4. 4 2

"""
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(4):
    print(num)

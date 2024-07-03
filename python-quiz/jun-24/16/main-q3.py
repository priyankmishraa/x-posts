"""
What will be the output?

1. 0 1 1 2
2. 1 1 2 3
3. 0 1 2 3
4. 1 2 3 5

"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = fibonacci(4)
for number in fib:
    print(number)

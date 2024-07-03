"""
What will be the output?

1. 3
2. 5
3. 8
4. 7

"""
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

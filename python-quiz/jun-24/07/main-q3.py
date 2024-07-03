"""
What will be the output?

1. 24
2. 12
3. 4
4. 120

"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

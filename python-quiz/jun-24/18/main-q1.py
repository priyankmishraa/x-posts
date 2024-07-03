"""
What will be the output?

1. 6
2. 8
3. 9
4. 12
"""
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))

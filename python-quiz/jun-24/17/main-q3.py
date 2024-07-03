"""
What will be the output?

1. 14
2. 12
3. 9
4. 29

"""

def sum_of_squares(n):
    if n == 0:
        return 0
    return n**2 + sum_of_squares(n-1)

print(sum_of_squares(3))

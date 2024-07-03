"""
What will be the output?

1. Result: 10
2. 10
3. Result: [1, 2, 3, 4]
4. Result: 4

"""

def add_prefix(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Result: {result}"
    return wrapper

@add_prefix
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_of_list([1, 2, 3, 4]))

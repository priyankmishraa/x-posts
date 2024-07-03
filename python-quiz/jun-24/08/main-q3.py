"""
What will be the output?

1. 5 Before function After function
2. Before function 5 After function
3. Before function After function 5
4. 2 3


"""

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def sum(a, b):
    return a + b

print(sum(2, 3))

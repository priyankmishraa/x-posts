"""
What will be the output?

1. Executing multiply 12 Executed multiply
2. Executing multiply 3 4 Executed multiply
3. Executing multiply Executed multiply 12
4. Executing multiply Executed multiply

"""
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Executed {func.__name__}")
        return result
    return wrapper

@log_execution
def multiply(a, b):
    return a * b

print(multiply(3, 4))

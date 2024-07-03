"""
What will be the output?

1. Starting function 0 1 2 Ending function
2. 0 1 2
3. 0 1 2 Starting function Ending function
4. Starting function Ending function

"""

def decorator(func):
    def wrapper():
        print("Starting function")
        func()
        print("Ending function")
    return wrapper

@decorator
def loop_function():
    for i in range(3):
        print(i)

loop_function()
